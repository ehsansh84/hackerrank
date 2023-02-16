import sys
from typing import List, NamedTuple, Tuple


class AssemblyOperation(NamedTuple):
    name: str
    duration: int
    dependencies: Tuple[str, ...]

def minimum_assembly_time(ops: List[AssemblyOperation]) -> int:
    tasks_dic = {task.name: {'duration': task.duration, 'dependencies': task.dependencies} for task in ops }
    def get_dependencies_times(task: AssemblyOperation):
        dep_times = []
        if not task.dependencies:
            return 0
        if 'dep_duration' in tasks_dic[task.name]:
            return tasks_dic[task.name]['dep_duration']
        for dep in task.dependencies:
            try:
                temp = AssemblyOperation(dep, int(tasks_dic[dep]['duration']), tasks_dic[dep]['dependencies'])
                dep_time = tasks_dic[dep]['duration'] + get_dependencies_times(temp)
                dep_times.append(dep_time)
            except KeyError:
                return -1
        t = max(dep_times)
        tasks_dic[task.name]['dep_duration'] = t
        return t
    all_task_times = []
    for item in ops:
        dep_time = get_dependencies_times(item)
        if dep_time == -1:
            return -1
        all_task_times.append(item.duration + dep_time)
    return max(all_task_times)


def main():
    ops = []
    with open('data-tc11') as f:
        for line in f.readlines():
            name, duration, *dependencies = line.rstrip().split()
            ops.append(AssemblyOperation(name, int(duration), dependencies))
    print(minimum_assembly_time(ops))


if __name__ == "__main__":
    main()
