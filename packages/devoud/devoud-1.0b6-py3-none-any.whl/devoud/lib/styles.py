from string import Template
from .svg import set_icon_color
from .devoud_data import *


class StylizedWindow:
    def __init__(self, user_settings, current_theme):
        self.user_settings = user_settings
        self.current_theme = current_theme

        # стандартная тема
        self.title_buttons_color = {
            "min": "#1D1F2A",
            "max": "#1D1F2A",
            "close": "#aa2f2f"
        }

        self.bg = '#282A3A'
        self.fg = '#eef1f1'
        self.light_color = '#3D3F59'

        self.search_box = {
            'bg': '#515375',
            'fg': '#eef1f1',
        }

        self.address_edit = {
            'bg': '#1D1F2A',
            'fg': '#dfdfdf',
            'border': '#515375'
        }

        self.button = {
            'bg': '#282a3a',
            'fg': '#eef1f1',
            'hover': '#3D3F59',
        }

        self.tab_widget = {
            "bg": "#282a3a",
            "fg": "#dfdfdf",
            "bg_select": "#515375",
            "fg_select": "#dfdfdf",
            "hover": "#3D3F59"
        }

        self.combobox = {
            'bg': '#515375',
            'fg': '#eef1f1',
            'select': '#515375',
            'item': '#3d3f59'
        }

        self.check_box = {
            'normal': '#1d1f2a',
            'checked': '#aa2f2f'
        }

        self.sections_panel = {
            'bg': '#1d1f2a',
            'fg': '#eef1f1',
            'select': '#515375',
            'hover': '#3D3F59'
        }

        self.widget = {
            'bg': '#363a4f',
            'fg': '#eef1f1'
        }

        self.widget_title = {
            'bg': '#1d1f2a',
            'fg': '#eef1f1'
        }

        self.widget_title_btn = {
            'bg': '#363a4f',
            'hover': '#515375'
        }

        self.chunk = '#aa2f2f'

        self.import_theme()
        set_icon_color(self)

    def import_theme(self):
        try:
            with open(f"./ui/themes/{self.current_theme}.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            print('[Стили]: Файл темы не найден', self.current_theme)
            return

        self.title_buttons_color = data['title_buttons_color']
        self.bg = data['bg']
        self.fg = data['fg']
        self.light_color = data['light_color']
        self.search_box = data['search_box']
        self.address_edit = data['address_edit']
        self.button = data['button']
        self.tab_widget = data['tab_widget']
        self.combobox = data['combobox']
        self.check_box = data['check_box']
        self.sections_panel = data['sections_panel']
        self.widget = data['widget']
        self.widget_title = data['widget_title']
        self.widget_title_btn = data['widget_title_btn']
        self.chunk = data['chunk']

    def browser_window(self):
        return Template("""
        QToolTip {
                background-color: $bg;
                color: $text;
                font: 10pt "Clear Sans Medium";
                border: 2px solid $line_edit_border;
                padding: 3px;
                border-radius: 0;
        }

        QWidget#widget_title {
                background: $widget_title_bg;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                border-bottom-left-radius: 0;
                border-bottom-right-radius: 0;
                outline: 0px;
        }

        QLabel#widget_title_text {
                padding-top: 2px;
                padding-bottom: 2px;
                background: none;
                font: 16pt 'Clear Sans Medium';
                color: $widget_title_fg;
        }

        QPushButton#widget_title_button {
                border: 0px;
                border-radius: 6px;
                background: $widget_title_btn_bg;
                font-size: 14px;
                padding: 2px;
        }

        QPushButton#widget_title_button:hover {
                background: $widget_title_btn_hover_bg;
        }

        QWidget#widget_content {
                background: $widget_bg; 
        }

        QWidget#widget_content QWidget {
                background: $widget_bg; 
        }

        QPushButton#add_tab_button {
                margin-left: 8px;
                margin-bottom: 5px;
                background: transparent;
                icon: url(./ui/custom/svg/add_tab.svg);
                border: none;
                border-radius: 6px;
        }

        QPushButton#add_tab_button:hover{
                background: $button_bg_hover;
        }

        QWidget {
                background: $bg;
                color: $text;
                font: 11pt "Clear Sans Medium";
                outline: 0;
        }

        QLabel#title_label {
                margin-left: 12px;
                margin-top: 5px;
        }

        #hide_button, #maximize_button {
                border: 2px solid transparent;
                image: url(./ui/custom/svg/hide.svg);
        }

        #hide_button:hover, #maximize_button:hover {
                background: $window_title_min_button;
        }

        #close_button {
                border: 2px solid transparent;
                image: url(./ui/custom/svg/close.svg);
        }

        #close_button:hover {
                background: $window_title_close_button;
                icon: none;
        }

        #find_widget {
                border-radius: 0;
        }

        QCheckBox::indicator {
                background: $indicator;
                border-radius: 6px;
        }
        QCheckBox::indicator:checked {
                background: $checked_indicator;
        }

        #find_widget_edit {
                background: $line_edit_bg;
                border-radius: 6px;
                padding: 4px;
        }

        #find_widget_previous_button {
                border-radius: 6px;
                padding: 4px;
                padding-right: 0px;
                padding-left: 0px;
                icon: url(./ui/custom/svg/arrow_left.svg)
        }

        #find_widget_next_button {
                border-radius: 6px;
                padding: 4px;
                padding-right: 0px;
                padding-left: 0px;
                icon: url(./ui/custom/svg/arrow_right.svg)
        }

        #find_widget_hide_button {
                border-radius: 6px;
                font-size: 14px;
                padding: 4px;
                padding-left: 6px;
                padding-right: 6px;
                background: $window_title_close_button;
        }

        QPushButton {
                border: none;
                border-radius: 6px;
        }

        QPushButton:hover {
                background: $button_bg_hover;
        }

        QPushButton::menu-indicator { 
                height: 0px;
                width: 0px;
        }

        QFrame#address_frame {
                background: $line_edit_bg;
                padding: 0;
                border-radius: 6px;
        }

        QPushButton#bookmark_button {
                border: none;
                background: transparent;
                border-top-right-radius: 6px;
                border-top-left-radius: 0px;
                border-bottom-right-radius: 6px;
                border-bottom-left-radius: 0px;
        }

        QPushButton#bookmark_button:hover {
                background: $search_box_bg;
        }

        QComboBox {
                padding: 0px 13px 0px 13px;
                background: $combobox_bg;
                color: $combobox_fg;
                border-top-left-radius: 6px;
                border-bottom-left-radius: 6px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
        }

        QComboBox::drop-down {
                width: 0px;
        }

        QComboBox QAbstractItemView {
                border: 0px;
                border-radius: 0;
        }

        QComboBox:hover {
                background: $combobox_select;
        }

        #search_box {
                border: none;
                padding: 0px 13px 0px 13px;
                background: $search_box_bg;
                color: $search_box_fg;
                border-top-left-radius: 6px;
                border-bottom-left-radius: 6px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
        }

        QLineEdit {
                background: transparent;
                color: $line_edit_fg;
                padding-left: 5px;
                border-radius: 0;
                selection-background-color: $line_edit_border;
        }

        QLineEdit:focus {
                border: 2px solid $line_edit_border;
        }
        
        QProgressBar {border: 0;}

        QProgressBar::chunk {background: $chunk;}

        """).substitute(text=self.fg,
                        bg=self.bg,
                        window_title_close_button=self.title_buttons_color['close'],
                        window_title_min_button=self.title_buttons_color['min'],
                        button_bg_hover=self.button['hover'],
                        widget_title_bg=self.widget_title['bg'],
                        widget_title_fg=self.widget_title['fg'],
                        sections_panel_bg=self.sections_panel['bg'],
                        sections_panel_hover=self.sections_panel['hover'],
                        sections_panel_select=self.sections_panel['select'],
                        widget_bg=self.widget['bg'],
                        widget_title_btn_bg=self.widget_title_btn['bg'],
                        widget_title_btn_hover_bg=self.widget_title_btn['hover'],
                        indicator=self.check_box['normal'],
                        checked_indicator=self.check_box['checked'],
                        line_edit_bg=self.address_edit['bg'],
                        line_edit_fg=self.address_edit['fg'],
                        line_edit_border=self.address_edit['border'],
                        combobox_bg=self.combobox['bg'],
                        combobox_fg=self.combobox['fg'],
                        combobox_item=self.combobox['item'],
                        combobox_select=self.combobox['select'],
                        chunk=self.chunk,
                        search_box_bg=self.search_box['bg'],
                        search_box_fg=self.search_box['fg'])

    def window_round(self, rounded_corners):
        return "border-radius: 12px" if rounded_corners else "border-radius: 0px"

    def BrowserTabWidget(self):
        return Template("""
        QTabWidget {
                background: $tab_widget_bg;
                border: 0px;
                padding: 0px;
        }

        QTabWidget::tab-bar {
                left: 42px;
                right: 35px;
        }

        QTabBar::tab {
                margin: 4px;
                margin-top: 6px;
                margin-bottom: 5px;
                border-radius: 6px;
                min-width: 100px;
                max-width: 200px;
                color: $tab_widget_fg;
                padding: 5px;
        }

        QTabBar::tab:text {
                padding-left: 5px;    
        }

        QTabWidget::pane {}

        QTabBar::tab:selected {
                background: $tab_widget_bg_select;
                color: $tab_widget_fg_select;
        }

        QTabBar::tab:!selected:hover {
                background: $tab_widget_bg_hover;
        }

        QTabBar::tab:!selected {
                background: $tab_widget_bg;
                color: $tab_widget_fg;
        }

        QTabBar QToolButton::right-arrow {
                image: url(./ui/custom/svg/arrow_right.svg);
        }

        QTabBar QToolButton::left-arrow {
                image: url(./ui/custom/svg/arrow_left.svg);
        }

        QTabBar::close-button {
                image: url(./ui/custom/svg/close_tab.svg);
                padding-right: 6px;
        }
        """).substitute(tab_widget_bg_hover=self.tab_widget['hover'],
                        tab_widget_bg=self.tab_widget['bg'],
                        tab_widget_bg_select=self.tab_widget['bg_select'],
                        tab_widget_fg_select=self.tab_widget['fg_select'],
                        tab_widget_fg=self.tab_widget['fg'])

    def context_menu(self):
        return Template('''
        QMenu {
                color: $text;
                background-color: $bg;
                border: 2px solid $border;
                border-radius: 6px;
        }

        QMenu::item {
                padding: 6px;
                padding-left: 6px;
                padding-right: 6px;
                background: transparent;
        }

        QMenu::item:selected {
                background: $bg_select;
                border-radius: 3px;
        }

        QMenu::separator {background-color: $border; height: 0.1em;}
        ''').substitute(text=self.fg,
                        bg=self.bg,
                        border=self.search_box['bg'],
                        bg_select=self.widget['bg'])

    def bookmarks_button(self, state=False):
        return f"icon: url(./ui/custom/svg/{'bookmark' if state else 'bookmark_empty'}.svg);"

    def control_page(self):
        return Template("""
        QWidget {
                color: $text;
                font: 12pt "Clear Sans Medium";
                border-bottom-left-radius: 6px;
                border-bottom-right-radius: 6px;
                border-top-right-radius: 0px;
                border-top-left-radius: 0px;
                outline: 0px;
        }


        QScrollBar:horizontal {
                background: $sections_panel_bg;
                max-height: 11px;
                border-radius: 4px;
                margin-top: 3px;
        }
    
        QScrollBar::handle:horizontal {
                background-color: $checked_indicator;
                min-width: 5px;
                border-radius: 4px;
        }
    
        QScrollBar::add-line:horizontal {
                border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
        }
    
        QScrollBar::sub-line:horizontal {
                border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
        }
    
        QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on {
                border-image: url(:/qss_icons/rc/right_arrow.png);
        }
    
    
        QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {
                border-image: url(:/qss_icons/rc/left_arrow.png);
        }
    
        QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
                background: none;
        }
    
    
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none;
        }
    
        QScrollBar:vertical {
                background: $sections_panel_bg;
                max-width: 11px;
                border-radius: 4px;
                margin-left: 3px;
        }
    
        QScrollBar::handle:vertical {
                background-color: $checked_indicator;
                min-height: 5px;
                border-radius: 4px;
        }
    
        QScrollBar::sub-line:vertical {
                border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
        }
    
        QScrollBar::add-line:vertical {
                border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
        }
    
        QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on {
                border-image: none;
        }
    
        QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {
                border-image: none;
        }
    
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
        }
    
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
        }

        QWidget#widget_title {
                background: $widget_title_bg;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                border-bottom-left-radius: 0;
                border-bottom-right-radius: 0;
                outline: 0px;
        }

        QLabel#widget_title_text {
                padding-top: 2px;
                padding-bottom: 2px;
                background: none;
                font: 16pt 'Clear Sans Medium';
                color: $widget_title_fg;
        }

        QPushButton#widget_title_button {
                border: 0px;
                border-radius: 6px;
                background: $widget_title_btn_bg;
                font-size: 14px;
                padding: 2px;
        }

        QPushButton#widget_title_button:hover {
                background: $widget_title_btn_hover_bg;
        }

        QWidget#widget_content {
                background: $widget_bg; 
        }

        QWidget#widget_content QWidget {
                background: $widget_bg; 
                color: $widget_fg;
        }

        QWidget#widget_content QLineEdit {
                background: $line_edit_bg;
                color: $line_edit_fg;
        }

        QWidget#widget_content QComboBox {
                background: $combobox_bg;
                color: $combobox_fg;
        }

        QCheckBox::indicator {
                background: $indicator;
                border-radius: 6px;
        }

        QCheckBox::indicator:checked {
                background: $checked_indicator;
        }

        QLineEdit {
                border: 2px solid $line_edit_border;
                selection-background-color: $line_edit_border;
                border-radius: 6px;
                padding-left: 7px;
                padding-right: 7px;
                padding-bottom: 1px;
                font: 11pt "Clear Sans Medium";
        }

        QComboBox {
                border: 0px;
                background: $combobox_bg;
                color: $combobox_fg;
                border-radius: 6px;
                padding: 0px 15px 0px 10px;
        }

        QComboBox::drop-down {
                width: 0px;
        }

        QComboBox QAbstractItemView {
                border: 0px;
                border-radius: 0px;
                background: $combobox_item;
                selection-background-color: $combobox_select;
        }

        #sections_panel {
                background: $sections_panel_bg;
                border-radius: 0;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
                min-width: 50px;
                max-width: 50px;
        }

        #sections_panel::item {
                border-radius: 0;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
        }

        QListWidget {
                show-decoration-selected: 0;
        }

        QListWidget::item {
                padding-left: 10px;
                border: 0;
                border-radius: 6px;
        }

        QListWidget::item:hover {
                background: $sections_panel_hover;
        }

        QListWidget::item:selected {
                background: $sections_panel_select;
                border-radius: 6px;
        }

        QToolTip {
                background-color: $bg;
                color: $text;
                font: 10pt "Clear Sans Medium";
                border: 2px solid $line_edit_border;
                padding: 3px;
        }
                           """).substitute(text=self.fg,
                                           bg=self.bg,
                                           widget_title_bg=self.widget_title['bg'],
                                           widget_title_fg=self.widget_title['fg'],
                                           sections_panel_bg=self.sections_panel['bg'],
                                           sections_panel_hover=self.sections_panel['hover'],
                                           sections_panel_select=self.sections_panel['select'],
                                           widget_bg=self.widget['bg'],
                                           widget_fg=self.widget['fg'],
                                           widget_title_btn_bg=self.widget_title_btn['bg'],
                                           widget_title_btn_hover_bg=self.widget_title_btn['hover'],
                                           indicator=self.check_box['normal'],
                                           checked_indicator=self.check_box['checked'],
                                           line_edit_bg=self.address_edit['bg'],
                                           line_edit_fg=self.address_edit['fg'],
                                           line_edit_border=self.address_edit['border'],
                                           combobox_bg=self.combobox['bg'],
                                           combobox_fg=self.combobox['fg'],
                                           combobox_item=self.combobox['item'],
                                           combobox_select=self.combobox['select'])
