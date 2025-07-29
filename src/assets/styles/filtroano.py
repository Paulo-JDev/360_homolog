# Em... src/assets/styles/filtroano.py

def get_filtro_container_style():
    """Retorna o CSS para o QFrame que contém o ícone e a ComboBox."""
    return """
        QFrame {
            border: 1px solid #CCCCCC;
            border-radius: 5px;
            background-color: #F3F3F3;
        }
    """

def get_filtro_ano_combo_style():
    """Retorna o CSS para a QComboBox (sem borda e fundo transparente)."""
    return """
        QComboBox {
            border: none; /* Remove a borda da ComboBox */
            background-color: transparent; /* Fundo transparente para misturar com o Frame */
            padding-left: 5px; /* Pequeno espaço interno à esquerda */
            color: #333333;
            font-size: 16px;
            font-weight: bold;
        }
        QComboBox::drop-down {
            border: none; /* Remove a borda da seta */
            padding-right: 5px;
        }
        QComboBox QAbstractItemView {
            border: 1px solid #CCCCCC;
            background-color: #F3F3F3;
            color: #333333;
            selection-background-color: #2C2F3F;
            selection-color: white;
            font-size: 14px;
        }
    """