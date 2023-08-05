"""Diodedance control library."""

import socket
import serial
from abc import ABC, abstractmethod
from typing import Optional, Final, Iterable
from time import sleep


class IncompleteCommand(Exception):
    """
    Command received by board lacked complete parts.

    Essentially, the board is rejecting the command because it is invalid.

    Usually caused by message corruption.
    Requires manual intervention, however is generally recoverable.
    Consider resending incomplete commands.

    Check link stability if this exception is frequently raised.
    """


class AheadCommand(Warning):
    """
    Command received by board is ahead of the board's idempotency counter.

    Essentially, the board is rejecting the command because it appears to be
    from the future.

    Usually caused by desynchronization of command sequence.
    Requires manual intervention, however is generally recoverable.
    Consider resending untimely commands.

    Clients will automatically correct themselves upon this warning.
    The board will safely ignore the command.

    Check if there are other clients interacting with the board if this
    warning is frequently raised.
    """


class BehindCommand(Warning):
    """
    Command received by board is behind the board's idempotency counter.

    Essentially, the board is rejecting the command because it appears to be
    from the past.

    Usually caused by desynchronization of command sequence.
    Requires manual intervention, however is generally recoverable.
    Consider resending untimely commands.

    Clients will automatically correct themselves upon this warning.
    The board will safely ignore the command.

    Check if there are other clients interacting with the board if this
    warning is frequently raised.
    """


class FailedCommand(Exception):
    """
    Command received by board failed.

    The reason for failure depends on the context of the command.
    Recover by troubleshooting your configuration and network conditions, and
    ensuring that the command instructed is valid.
    """


class Client(ABC):
    """
    Base client for controlling a board.

    Provides common abstractions for derivatives.
    Not intended for direct use by the end-user,
    unless for writing new clients.
    """

    NO_CMD_ARG: Final[str] = "X"

    def __init__(self):
        """Initialize client."""
        self.idempotency = 1

    def _idempotency_uptick(self, at: Optional[int] = None) -> None:
        """Safely increase idempotency counter with respect to overflow."""
        self.idempotency = (at if at is not None else self.idempotency) + 1
        if self.idempotency > 4294967295:
            self.idempotency = 1

    @abstractmethod
    def _send(self, msg: str) -> str:
        """Exchange raw messages through specialized interface."""
        pass

    def send(self, cmd: int, arg: str, auto_retry: bool = True) -> None:
        """Send command to board."""
        reply = self._send(str(self.idempotency) + " " + str(cmd) + " " + arg)
        status, at = reply.split(" ")

        if at == "X":
            if status == "FAIL":
                raise IncompleteCommand(str(cmd) + "not valid.")
            return

        at = int(at)

        if status == "OK":
            if at == self.idempotency:
                self._idempotency_uptick()
            else:
                self._idempotency_uptick(at)
                if auto_retry:
                    self.send(cmd, arg, False)
                else:
                    raise BehindCommand(
                        str(self.idempotency) + " behind " + str(at) + ".")

            return
        elif status == "NIAA":
            self._idempotency_uptick(at)
            if auto_retry:
                self.send(cmd, arg, False)
            else:
                raise AheadCommand(
                    str(self.idempotency) + " ahead " + str(at) + ".")
        else:
            raise FailedCommand(str(self.idempotency) + " failed.")
            self._idempotency_uptick()


class SerialClient(Client):
    """
    Serial client for physical links.

    Intended for configuring networking, and running debug functions.
    """

    CMD_SET_SSID: Final[int] = 0
    CMD_SET_PASSWORD: Final[int] = 1
    CMD_RESTART_WIFI: Final[int] = 2
    CMD_RESTART_INET: Final[int] = 3
    CMD_SET_PORT: Final[int] = 4
    CMD_SET_IP_FIRST: Final[int] = 5
    CMD_SET_IP_SECOND: Final[int] = 6
    CMD_SET_IP_THIRD: Final[int] = 7
    CMD_SET_IP_FOURTH: Final[int] = 8
    CMD_SET_GATEWAY_FIRST: Final[int] = 9
    CMD_SET_GATEWAY_SECOND: Final[int] = 10
    CMD_SET_GATEWAY_THIRD: Final[int] = 11
    CMD_SET_GATEWAY_FOURTH: Final[int] = 12
    CMD_SET_SUBNET_FIRST: Final[int] = 13
    CMD_SET_SUBNET_SECOND: Final[int] = 14
    CMD_SET_SUBNET_THIRD: Final[int] = 15
    CMD_SET_SUBNET_FOURTH: Final[int] = 16
    CMD_RESET: Final[int] = 17
    CMD_RESTART: Final[int] = 18

    def __init__(self, port: str, timeout: float = 60):
        """Initialize client."""
        super().__init__()
        self.serial = serial.Serial(port=port, timeout=timeout)
        if not self.serial.is_open:
            self.serial.open()

        # board sometimes spews a false failure message.
        # this is a hack to disregard the garbage sent.
        sleep(1)
        self.serial.flush()

    def _send(self, msg: str) -> str:
        self.serial.write((msg + "\n").encode("ascii"))
        return self.serial.read_until().decode("utf-8")

    @staticmethod
    def _check_ip(octets: Iterable[int]):
        """Check if integers are ok as octets for address or subnet mask."""
        if len(octets) != 4:
            raise ValueError("Invalid number of octets to qualify as address.")

        if any([(i not in range(0, 256)) for i in octets]):
            raise ValueError("Octets must be between 0 to 255 inclusive.")

    def set_ip(self, address: Iterable[int]):
        """Set the static IP address of the board."""
        SerialClient._check_ip(address)

        for i in range(4):
            self.send(SerialClient.CMD_SET_IP_FIRST + i, str(address[i]))

    def set_gateway(self, address: Iterable[int]):
        """Set the gateway IP address of the board."""
        SerialClient._check_ip(address)

        for i in range(4):
            self.send(SerialClient.CMD_SET_GATEWAY_FIRST + i, str(address[i]))

    def set_subnet(self, subnet: Iterable[int]):
        """Set the subnet mask of the board."""
        SerialClient._check_ip(subnet)

        for i in range(4):
            self.send(SerialClient.CMD_SET_SUBNET_FIRST + i, str(subnet[i]))

    def set_port(self, port: int):
        """Set the port for the board to listen for UDP packets on."""
        if port not in range(1, 65536):
            raise ValueError("Port must be between to 1 to 65535 inclusive.")

        self.send(SerialClient.CMD_SET_PORT, str(port))


class NetClient(Client):
    """
    Network client for wireless links.

    Intended for LED control.
    """

    CMD_CLEAR_ALL_LEDS: Final[int] = 0
    CMD_SET_LED: Final[int] = 1

    def __init__(self, host: str, port: int, local: str = "0.0.0.0"):
        """Initialize client."""
        super().__init__()
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver.bind(("0.0.0.0", port))
        self.ip = host
        self.port = port

    def _send(self, msg: str) -> str:
        self.sender.sendto((msg + "\n").encode("ascii"), (self.ip, self.port))
        while True:
            data, address = self.receiver.recvfrom(1024)
            if address[0] == self.ip:
                break
        return data.decode("utf-8")

    def clear_leds(self):
        """Clear all LEDs."""
        self.send(NetClient.CMD_CLEAR_ALL_LEDS, NetClient.NO_CMD_ARG)

    def set_led(self, x: int, y: int, r: int, g: int, b: int):
        """Set LED at 2D coordinate to color."""
        if x not in range(0, 12):
            raise ValueError("Coordinate X must be within 0 to 11 inclusive.")

        if y not in range(0, 12):
            raise ValueError("Coordinate Y must be within 0 to 11 inclusive.")

        if any([i not in range(0, 256) for i in [r, g, b]]):
            raise ValueError("Color values must be within 0 to 255 inclusive.")

        self.send(
            NetClient.CMD_SET_LED,
            str(r) + " " + str(g) + " " + str(b) + " " + str(x) + " " + str(y))
