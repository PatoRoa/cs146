# You are the sysadmin for a big tech company, and you have to estimate the amount of servers you need to handle some
# long-running jobs.
#
# One server can handle only one job at once.
# One job can only be executed by one server at once.
#
# Once a server has finished executing its current job, it can be reassigned to a new job.
#
# Given an array of time intervals 'intervals' where intervals[i] = [start_i, end_i], representing the start and end
# time for a particular job that needs to be executed, return the minimum number of servers required to run all jobs.
#
# Constraints:
# 1 <= intervals.length <= 10^4
# 0 <= start_i < end_i <= 10^6

# Announced Test Cases:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Explanation: We need one server for the job that starts at 0.
# For the job that starts at 5, we need to assign another server, since the first one is busy.
# We can then reassign that same server for the job that starts at 15.

# Input: intervals = [[0,1],[1,2],[2,3]]
# Output: 1
# Explanation: We need one server for the job that starts at 0.
# We can then reassign that same server for the job that starts at 1, and then reassign it for the job that starts at 2.
from typing import List

MAX = 10000000


def minMeetingRooms(intervals: List[List[int]]) -> int:
    servers = 0
    intervals.sort()

    starts = []
    ends = []

    for i in range(len(intervals)):
        starts.append(intervals[i][0])
        ends.append(intervals[i][1])

    for j in range(ends[-1]):
        if j in starts:
            servers += 1
        if j in ends:
            servers -= 1

    print(servers)
    return servers


k = [[0, 30], [5, 10], [15, 20]]

minMeetingRooms(k)
