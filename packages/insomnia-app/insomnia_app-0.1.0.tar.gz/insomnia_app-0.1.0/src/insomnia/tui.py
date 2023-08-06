import operator
import time
from dataclasses import dataclass, field
from typing import List

import humanize
import psutil
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn
from textual.app import App
from textual.color import Color
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Footer, Header, Static

CHECK_DELAY = 1
MIN_SLEEP_DURATION = 60
ACTIVE_TIME_SCALE = 3600
PROCESS_CPU_THRESHOLD = 0.1


@dataclass(order=True)
class ProcessStats:
    """Process statistics like name and cpu times."""

    name: str
    user_time: float
    sys_time: float
    total_time: float = field(init=False)

    def __post_init__(self):
        self.total_time = self.user_time + self.sys_time

    def __add__(self, other):
        return ProcessStats(
            self.name, self.user_time + other.user_time, self.sys_time + other.sys_time
        )

    def __sub__(self, other):
        return ProcessStats(
            self.name, self.user_time - other.user_time, self.sys_time - other.sys_time
        )


def get_process_statistics():
    """Get process statistics like name and cpu times.

    Returns:
        A dict where the keys are made up of tuples containing the
        process ID and process creation time. This ensures that every process
        gets a unique key, even if process IDs are reused. Each value is a
        ProcessStats instance.
    """
    return {
        (p.info["pid"], p.info["create_time"]): ProcessStats(
            name=p.info["name"],
            user_time=p.info["cpu_times"][0],
            sys_time=p.info["cpu_times"][1],
        )
        for p in psutil.process_iter(attrs=["pid", "create_time", "name", "cpu_times"])
        if p.info["cpu_times"] is not None
    }


class SleepinessDisplay(Static):
    sleepiness = reactive(0.0)

    def on_mount(self):
        self.progressbar = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            TaskProgressColumn(),
        )
        self.sleepingtask = self.progressbar.add_task("Steady sleep", total=1.0)

    def watch_sleepiness(self, sleepiness):
        self.log(f"Sleepiness update: {sleepiness}")
        self.progressbar.update(self.sleepingtask, completed=sleepiness)
        self.update(self.progressbar)


class CurrentActivityWidget(Static):
    is_tracking = reactive(True)

    def toggle_is_tracking(self):
        self.is_tracking = not self.is_tracking

    def watch_is_tracking(self, is_tracking):
        if is_tracking:
            self.query_one("#tracking_state").update("Tracking...")
        else:
            self.query_one("#tracking_state").update("Tracking paused...")

    def compose(self):
        yield Static(id="tracking_state")
        yield SleepinessDisplay(id="sleepiness")


class InsomniaApp(App):
    """An app for tracking wakeful moments during supposed sleep periods."""

    CSS_PATH = "insomnia.css"

    BINDINGS = [
        ("t", "toggle_tracking_state()", "Toggle tracking"),
        ("q", "quit()", "Quit"),
    ]

    sleeping = awake = 0

    def compose(self):
        self.t_prev_wake_event = self.t_prev_check = time.time()
        self.clear_process_stats()
        self.sleep_timer = self.set_interval(CHECK_DELAY, self.check_for_sleep)
        yield Header(show_clock=True)
        yield Footer()
        yield Container(id="past_activity")
        yield CurrentActivityWidget(id="current_activity")

    async def action_toggle_tracking_state(self):
        if self.query_one("#current_activity").is_tracking:
            # Stop tracking sleeps, log active period first
            self.update_process_stats()
            await self.log_active_period(
                active_duration=self.t_prev_check - self.t_prev_wake_event,
            )
            tracking_msg = Static("Stopped tracking sleeps", classes="log stopped")
            self.awake += time.time() - self.t_prev_check
            self.sleep_timer.pause()
        else:
            # Start tracking sleeps
            tracking_msg = Static("Started tracking sleeps", classes="log started")
            self.t_prev_wake_event = self.t_prev_check = time.time()
            # Store baseline process statistics
            self.clear_process_stats()
            self.sleep_timer.resume()
        self.query_one("#current_activity").toggle_is_tracking()
        await self.query_one("#past_activity").mount(tracking_msg)
        tracking_msg.scroll_visible()

    async def check_for_sleep(self):
        """Check if computer was sleeping since last check.

        This method checks the elapsed time since the previous check. If more
        time has passed then MIN_SLEEP_DURATION it assumes that the computer has
        been sleeping. It is therefore important that you call this method
        regularly. Say, once per second.

        """
        now = time.time()
        delta_prev_check = now - self.t_prev_check
        if delta_prev_check > MIN_SLEEP_DURATION:
            # Just woke up from sleep, log active and sleep periods
            await self.log_active_period(
                active_duration=self.t_prev_check - self.t_prev_wake_event,
            )
            await self.log_sleep_period(
                sleep_duration=delta_prev_check,
            )
            # Update timestamps and durations
            self.t_prev_wake_event = now
            self.sleeping += delta_prev_check
        else:
            # Still active
            self.update_process_stats()
            self.awake += delta_prev_check
        # Update common timestamp and sleepiness
        self.t_prev_check = now
        self.query_one("#sleepiness").sleepiness = self.sleeping / (
            self.awake + self.sleeping
        )

    async def log_sleep_period(self, sleep_duration):
        """Log sleeping period.

        Add a log entry for the previous sleeping period.

        Args:
            sleep_duration (float): duration of sleeping period in seconds.
        """
        log_slept = Static(
            f"{time.ctime(self.t_prev_check)} — Slept for {humanize.precisedelta(sleep_duration)}",
            classes="log slept",
        )
        await self.query_one("#past_activity").mount(log_slept)
        log_slept.scroll_visible()

    async def log_active_period(self, active_duration):
        """Log previous active period.

        Add a log entry for the previous active period.

        Args:
            active_duration (float): duration of active period.
        """
        process_msg = ", ".join(
            [
                f"{p.name} ({p.total_time / active_duration * 100:.0f}%)"
                for p in self.get_cpu_intensive_processes(active_duration)
            ]
        )

        log_active = Static(
            f"{time.ctime(self.t_prev_wake_event)} — Active for {humanize.precisedelta(active_duration)}\n"
            f"Most active processes: [bold]{process_msg}",
            classes="log active",
        )
        log_active.styles.background = self.make_active_color(active_duration)
        await self.query_one("#past_activity").mount(log_active)
        log_active.scroll_visible()

    def make_active_color(self, active_duration):
        """Generate a background color for the active widget.

        Generate a background color from a continous gradient starting at green
        and changing via yellow into red. Green colours are generated for short
        durations and red colors for long durations.

        Args:
            active_duration (float): The duration of the active period.
        """
        factor = active_duration / ACTIVE_TIME_SCALE
        if factor > 1.0:
            factor = 1.0
        return Color(48, 54, 60).blend(Color(96, 0, 0), factor)

    def clear_process_stats(self):
        """Clear process statistics."""
        self.baseline_stats = get_process_statistics()
        self.process_stats = {}

    def update_process_stats(self):
        """Update process statistics."""
        self.process_stats |= get_process_statistics()

    def get_cpu_intensive_processes(self, active_duration) -> List[ProcessStats]:
        """Calculate CPU usage for all processes.

        Using the stored baseline and periodically gathered statistics this
        method calculates the CPU usage times of processes during the active
        period. The list is sorted on total CPU time (most-intensive processes
        first). This method yields ProcessStats instances until the total cpu
        time used by a process is less than PROCESS_CPU_THRESHOLD. The remaining
        processes use even less CPU and are not considered to be important.

        Args:
            active_duration (float): duration of the active period

        Returns:
            An interator yielding ProcessStats sorted on CPU total time in
                descending order up to a threshold.
        """
        cumulative = {}
        for key, latest_stats in self.process_stats.items():
            single_process_stats = latest_stats - self.baseline_stats.get(
                key, ProcessStats(None, 0, 0)
            )
            # Combine cpu times for processes with the same name
            cumulative[latest_stats.name] = (
                cumulative.get(latest_stats.name, ProcessStats(latest_stats.name, 0, 0))
                + single_process_stats
            )
        # sort on total time
        processes = sorted(
            cumulative.values(),
            key=operator.attrgetter("total_time"),
            reverse=True,
        )
        # yield processes until time exceeds threshold
        for process in processes:
            if process.total_time / active_duration > PROCESS_CPU_THRESHOLD:
                yield process
            else:
                break


def main():
    app = InsomniaApp()
    app.run()


if __name__ == "__main__":
    main()
