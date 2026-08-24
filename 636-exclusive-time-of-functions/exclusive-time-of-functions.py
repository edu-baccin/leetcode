class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            code, kind, time = log.split(":")
            time = int(time)

            if kind == "start":
                if stack:
                    result[int(stack[-1])] += time - prev_time
                stack.append(code)
                prev_time = time
            else:
                ended_id = stack.pop()
                result[int(ended_id)] += time - prev_time + 1
                prev_time = time + 1

        return result