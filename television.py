class Television:
    """A simple television class with power, mute, channel, and volume controls."""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television with default power, mute, volume, and channel settings."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the television if it is powered on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by one, wrapping to the minimum channel if needed."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by one, wrapping to the maximum channel if needed."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one and unmute the television if it is powered on."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one and unmute the television if it is powered on."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return a string showing the current power, channel, and volume settings."""
        if self.__muted:
            volume = 0
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
