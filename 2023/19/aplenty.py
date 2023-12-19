ACCEPTED = "A"
REJECTED = "R"

def parse_input(lines):
    workflows = {}
    parts = []

    def parse_workflow(s):
        name, wf = s.split("{")
        wf = wf.strip("{}").split(",")
        default = wf.pop(-1)

        def workflow(part):
            for rule in wf:
                cond, loc = rule.split(":")
                if len(rule.split("<")) == 2:
                    key, num = cond.split("<")
                    if part[key] < int(num):
                        return loc
                elif len(rule.split(">")) == 2:
                    key, num = cond.split(">")
                    if part[key] > int(num):
                        return loc
            return default

        return name, workflow

    def parse_part(s):
        d = {}
        for a in s.strip("{}").split(","):
            k, v = a.split("=")
            d[k] = int(v)
        return d

    workflow_mode = True
    for l in lines:
        if l == "":
            workflow_mode = False
            continue
        if workflow_mode:
            k, v = parse_workflow(l)
            workflows[k] = v
        else:
            parts.append(parse_part(l))

    return workflows, parts


def aplenty(lines):
    workflows, parts = parse_input(lines)
    total = 0
    for part in parts:
        key = "in"
        while key not in {ACCEPTED, REJECTED}:
            key = workflows[key](part)
        if key == ACCEPTED:
            total += sum(part.values())
    return total


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(aplenty(lines))
