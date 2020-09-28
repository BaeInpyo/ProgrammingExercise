import bisect

def string_to_num(string):
    """ convert time string to number """
    hour, minute, second = string.split(":")
    return int(hour)*3600 + int(minute)*60 + int(second)

def num_to_string(num):
    hour = num // 3600
    minute = (num - 3600*hour) // 60
    second = (num - 3600*hour - 60*minute)
    return str(hour).rjust(2, "0") + ":" + str(minute).rjust(2, "0") + ":" + str(second).rjust(2, "0")

def solution(play_time, adv_time, logs):
    # points is sorted on (time, position)
    points = []
    for log in logs:
        start, end = log.split("-")
        start = string_to_num(start)
        end = string_to_num(end)
        bisect.insort(points, (start, "x"))
        bisect.insort(points, (end, "y"))
        
    intervals = []
    count = 0
    prev = 0
    for (time, pos) in points:
        if pos == "x":
            # [prev, pos] = count
            intervals.append((prev, time, count))
            count += 1
            prev = time
        elif pos == "y":
            intervals.append((prev, time, count))
            count -= 1
            prev = time
            
    # pop intervals starting with 00:00:00
    intervals = intervals[1:]
    if intervals[0][0] != 0:
        intervals.insert(0, (0, intervals[0][0], 0))
        
    if intervals[-1][1] != string_to_num(play_time):
        intervals.append((intervals[-1][1], string_to_num(play_time), 0))
        
    max_length = 0
    pos = None
    # interval is prepared
    for (idx, (start, end, freq)) in enumerate(intervals):
        # start is start of ad
        curr_length = 0
        for jdx in range(idx, len(intervals)):
            start_, end_, freq_ = intervals[jdx]
            if start_ > start + string_to_num(adv_time):
                break
            end_ = min(end_, start + string_to_num(adv_time))
            if end_ >= start_:
                curr_length += (end_ - start_) * freq
            
        if max_length < curr_length:
            pos = start
        
        # start is end of ad
        


solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	)
