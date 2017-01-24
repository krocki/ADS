# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-24 14:42:59
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-24 15:01:26
def canAttendMeetings(intervals):
    
    """
    :type intervals: List[Interval]
    :rtype: bool
    """

    intervals.sort(key=lambda x: x.start)
    
    #determine if there is an intersection
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end: return False
    
    #no intersection
    return True

print canAttendMeetings([[2,7]])
