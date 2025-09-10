"""
Color management utilities for the visualization
"""

from config.settings import COLORS

class ColorManager:
    def __init__(self, theme='default'):
        """
        Initialize color manager with a theme

        Args:
            theme: Color theme name
        """
        self.theme = theme
        self.colors = COLORS.copy()
        self.custom_colors = {}

    def get_color(self, color_name):
        """
        Get color by name

        Args:
            color_name: Name of the color

        Returns:
            Color hex string
        """
        # Check custom colors first
        if color_name in self.custom_colors:
            return self.custom_colors[color_name]

        # Fall back to default colors
        return self.colors.get(color_name, '#000000')

    def set_custom_color(self, color_name, color_value):
        """
        Set a custom color

        Args:
            color_name: Name of the color
            color_value: Hex color string
        """
        self.custom_colors[color_name] = color_value

    def get_bar_color(self, state):
        """
        Get bar color based on state

        Args:
            state: Bar state ('default', 'comparing', 'swapping', etc.)

        Returns:
            Color hex string
        """
        color_map = {
            'default': self.get_color('bar_default'),
            'comparing': self.get_color('bar_comparing'),
            'swapping': self.get_color('bar_swapping'),
            'sorted': self.get_color('bar_sorted'),
            'pivot': self.get_color('bar_pivot'),
            'current': self.get_color('bar_current')
        }

        return color_map.get(state, self.get_color('bar_default'))

    def get_theme_colors(self):
        """
        Get all colors for current theme

        Returns:
            Dictionary of theme colors
        """
        theme_colors = self.colors.copy()
        theme_colors.update(self.custom_colors)
        return theme_colors

    def apply_theme(self, theme_name):
        """
        Apply a predefined theme

        Args:
            theme_name: Name of the theme to apply
        """
        themes = {
            'dark': {
                'background': '#1a1a1a',
                'surface': '#2d2d2d',
                'text': '#ffffff',
                'bar_default': '#3498db',
                'bar_comparing': '#e74c3c',
                'bar_swapping': '#f39c12',
                'bar_sorted': '#2ecc71',
                'bar_pivot': '#9b59b6'
            },
            'light': {
                'background': '#f8f9fa',
                'surface': '#ffffff',
                'text': '#212529',
                'bar_default': '#0d6efd',
                'bar_comparing': '#dc3545',
                'bar_swapping': '#fd7e14',
                'bar_sorted': '#198754',
                'bar_pivot': '#6f42c1'
            },
            'high_contrast': {
                'background': '#000000',
                'surface': '#ffffff',
                'text': '#ffffff',
                'bar_default': '#0000ff',
                'bar_comparing': '#ff0000',
                'bar_swapping': '#ffff00',
                'bar_sorted': '#00ff00',
                'bar_pivot': '#ff00ff'
            }
        }

        if theme_name in themes:
            self.theme = theme_name
            self.colors.update(themes[theme_name])

    def interpolate_color(self, color1, color2, factor):
        """
        Interpolate between two colors

        Args:
            color1: First color (hex string)
            color2: Second color (hex string)
            factor: Interpolation factor (0-1)

        Returns:
            Interpolated color hex string
        """
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

        rgb1 = hex_to_rgb(color1)
        rgb2 = hex_to_rgb(color2)

        interpolated_rgb = tuple(
            rgb1[i] + factor * (rgb2[i] - rgb1[i]) for i in range(3)
        )

        return rgb_to_hex(interpolated_rgb)
