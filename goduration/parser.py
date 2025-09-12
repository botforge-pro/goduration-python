from datetime import timedelta


def parse(duration_str: str) -> timedelta:
    if not isinstance(duration_str, str):
        raise TypeError(f"Expected string, got {type(duration_str)}")
    
    s = duration_str.strip()
    if not s:
        raise ValueError("Empty duration string")
    
    is_negative = s.startswith('-')
    if is_negative:
        s = s[1:]
    
    total_minutes = 0
    i = 0
    
    while i < len(s):
        # Parse number (including fractional)
        num_start = i
        while i < len(s) and (s[i].isdigit() or s[i] == '.'):
            i += 1
        
        if i == num_start:
            raise ValueError(f"Expected number at position {i}")
        
        num = float(s[num_start:i])
        
        # Parse unit (1-2 chars)
        if i >= len(s):
            raise ValueError(f"Missing unit after number {num}")
        
        unit_start = i
        if i < len(s) - 1 and s[i:i+2] in ['ns', 'us', 'µs', 'μs', 'ms']:
            unit = s[i:i+2]
            i += 2
        else:
            unit = s[i]
            i += 1
        
        # Convert to minutes
        if unit == 'ns':
            total_minutes += num / (1000 * 1000 * 1000 * 60)
        elif unit in ['us', 'µs', 'μs']:
            total_minutes += num / (1000 * 1000 * 60)
        elif unit == 'ms':
            total_minutes += num / (1000 * 60)
        elif unit == 's':
            total_minutes += num / 60
        elif unit == 'm':
            total_minutes += num
        elif unit == 'h':
            total_minutes += num * 60
        else:
            raise ValueError(f"Invalid unit '{unit}', expected ns, us, ms, s, m, or h")
    
    if is_negative:
        total_minutes = -total_minutes
        
    return timedelta(minutes=total_minutes)