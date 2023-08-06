def hms_to_s(hms):
    """
    converts a duration expressed in hours, minutes, seconds into seconds.
    
    inputs:
    - hms: duration (hours, minutes, seconds) - type: tuple
        - hours - type: (int, float)
        - minutes - type: (int, float)
        - seconds - type: (int, float)
    
    returns:
    - s: duration in seconds - type: float
    or
    - None
    """
    
    if not isinstance(hms, tuple):
        return
    
    if not len(hms) == 3:
        return
    
    hours, minutes, seconds = hms
    
    if not isinstance(hours, (int, float)) or not isinstance(minutes, (int, float)) or not isinstance(seconds, (int, float)):
        return
    
    if not 0 <= hours or not 0 <= minutes or not 0 <= seconds:
        return
    
    return float(hours*3600. + minutes*60. + seconds)