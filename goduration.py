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
        # Parse number
        num_start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        
        if i == num_start:
            raise ValueError(f"Expected number at position {i}")
        
        num = int(s[num_start:i])
        
        # Parse unit
        if i >= len(s):
            raise ValueError(f"Missing unit after number {num}")
        
        unit = s[i]
        if unit == 'h':
            total_minutes += num * 60
        elif unit == 'm':
            total_minutes += num
        else:
            raise ValueError(f"Invalid unit '{unit}', expected 'h' or 'm'")
        
        i += 1
    
    if is_negative:
        total_minutes = -total_minutes
        
    return timedelta(minutes=total_minutes)