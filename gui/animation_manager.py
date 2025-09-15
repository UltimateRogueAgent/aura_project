from PyQt6.QtWidgets import QWidget, QScrollArea, QProgressBar
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QPoint

class AnimationManager:
    """
    Manages common UI animations for the application, providing a simple
    interface for creating smooth and visually appealing transitions.
    """

    def fade_in(self, widget: QWidget, duration: int = 300):
        """
        Fades a widget in by animating its window opacity.

        Args:
            widget: The QWidget to animate.
            duration: The duration of the animation in milliseconds.
        """
        animation = QPropertyAnimation(widget, b"windowOpacity")
        animation.setDuration(duration)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def slide_in(self, widget: QWidget, direction: str = "left", duration: int = 300):
        """
        Slides a widget in from a specified direction.

        Args:
            widget: The QWidget to animate.
            direction: The direction from which to slide in ('left', 'right', 'top', 'bottom').
            duration: The duration of the animation in milliseconds.
        """
        start_pos = widget.pos()
        end_pos = widget.pos()
        if direction == "left":
            start_pos.setX(-widget.width())
        elif direction == "right":
            start_pos.setX(widget.parent().width())
        elif direction == "top":
            start_pos.setY(-widget.height())
        else: # bottom
            start_pos.setY(widget.parent().height())

        animation = QPropertyAnimation(widget, b"pos")
        animation.setDuration(duration)
        animation.setStartValue(start_pos)
        animation.setEndValue(end_pos)
        animation.setEasingCurve(QEasingCurve.OutCubic)
        animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def smooth_scroll(self, scroll_area: QScrollArea, target: int, duration: int = 500):
        """
        Smoothly scrolls a QScrollArea to a target vertical position.

        Args:
            scroll_area: The QScrollArea to animate.
            target: The target vertical scrollbar value.
            duration: The duration of the animation in milliseconds.
        """
        animation = QPropertyAnimation(scroll_area.verticalScrollBar(), b"value")
        animation.setDuration(duration)
        animation.setStartValue(scroll_area.verticalScrollBar().value())
        animation.setEndValue(target)
        animation.setEasingCurve(QEasingCurve.InOutCubic)
        animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def progress_animation(self, progress_bar: QProgressBar, end_value: int, duration: int = 1000):
        """
        Animates a QProgressBar from its current value to an end value.

        Args:
            progress_bar: The QProgressBar to animate.
            end_value: The target value for the progress bar.
            duration: The duration of the animation in milliseconds.
        """
        animation = QPropertyAnimation(progress_bar, b"value")
        animation.setDuration(duration)
        animation.setStartValue(progress_bar.value())
        animation.setEndValue(end_value)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)
