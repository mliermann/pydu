from typing import Union

def dotted_netmask(mask: Union[int, str]) -> str: ...
def is_ipv4(ip: str) -> bool: ...
def is_ipv6(ip: str) -> bool: ...
def ip2int(ip_str) -> int: ...
def int2ip(ip_int: int) -> int: ...
