from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QEvent

class HoverFrame(QFrame):
    """
    Um QFrame customizado que muda seu estilo quando o mouse
    passa por cima, imitando o comportamento de um botão.
    """
    def __init__(self, normal_style, hover_style, parent=None):
        super().__init__(parent)
        self.normal_style = normal_style
        self.hover_style = hover_style
        # Começa com o estilo normal
        self.setStyleSheet(self.normal_style)

    def enterEvent(self, event: QEvent):
        """Chamado quando o mouse entra no widget."""
        self.setStyleSheet(self.hover_style)
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        """Chamado quando o mouse sai do widget."""
        self.setStyleSheet(self.normal_style)
        super().leaveEvent(event)