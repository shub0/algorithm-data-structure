'''
here are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

2. Course Schedule 2
Return a possible path
'''

class Solution(object):
    def buildGraph(self, prerequisites, numCourses):
        graph = { course: set() for course in range(numCourses) }
        depency = { course: 0 for course in range(numCourses) }
        for (course, pre) in prerequisites:
            if course not in graph[pre]:
                graph[pre].add(course)
                depency[course] += 1
        return graph, depency

    def findPath(self, numCourses, prerequisites):
        graph, depency = self.buildGraph(prerequisites, numCourses)
        path = list()
        valid_courses = filter( lambda course: depency[course] == 0, range(numCourses) )

        while (len(valid_courses) > 0):
            course = valid_courses.pop()
            path.append(course)
            for next_class in graph[course]:
                depency[next_class] -= 1
                if depency[next_class] == 0:
                    valid_courses.append(next_class)
        return path

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return len(self.findPath(numCourses, prerequisites)) == numCourses


    def findOrder(self, numCourses, prerequisites):
        path = self.findPath(numCourses, prerequisites)
        return path if len(path) == numCourses else []

solution = Solution()
print solution.canFinish(10, [[5,8],[3,5],[1,9],[4,5],[1,9],[0,2],[7,8],[4,9]])
