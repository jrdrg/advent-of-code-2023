import util

example_input = r"""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

example_input2 = r"""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

input_str = r"""
&kl -> ll
%vd -> ff, mb
%dx -> hb, fx
%jj -> xt, th
%ld -> fq, ff
%bn -> ff, lg
%mv -> hb, mx
%mx -> xp
%qm -> gz, tj
%zd -> zp
%tq -> mf
&vm -> ll
%qr -> jj
%bv -> th, lr
%rf -> lq, tj
broadcaster -> lp, fn, tp, zz
%rk -> rc, th
&tj -> xh, gv, gz, bt, ct, vb, lp
%dg -> rf, tj
%xt -> rk, th
%fq -> ff
%gz -> dg
%rl -> hb
%rc -> st, th
%km -> fz, hb
%gv -> ct
%lr -> tq
%lg -> vd
%jh -> th
%rs -> sq, ff
%bt -> kc
%mf -> th, qr
%xf -> km
%tp -> hb, sv
%ch -> hb, mv
%xp -> hb, xf
%xh -> js
%fz -> hb, dx
%zp -> bn
&kv -> ll
&ll -> rx
%zz -> fj, ff
%lp -> gv, tj
&vb -> ll
&th -> tq, lr, vm, fn, qr
%sq -> zd, ff
%st -> th, jh
%fx -> rl, hb
%fj -> rs
%lq -> tj
%fn -> th, bv
%ct -> xh
&ff -> kl, zd, lg, zz, fj, zp
%js -> tj, bt
%mb -> ld, ff
&hb -> sv, xf, kv, tp, mx
%kc -> qm, tj
%sv -> ch
"""

class Module:
    name: str
    destination_modules: list[str] = []
    def __init__(self, name: str, destination_modules: list[str]) -> None:
        self.name = name
        self.destination_modules = destination_modules
    def __repr__(self) -> str:
        return self.name + " -> " + self.destination_modules.__repr__()
    def receive_pulse(self, src: str, pulse: str):
        print("Unknown:", self.name, src, pulse)
        return []

class BroadcasterModule(Module):
    def receive_pulse(self, src: str, pulse: str):
        # print("Broadcaster:", src, pulse)
        return [(self.name, m, pulse) for m in self.destination_modules]


class FlipFlopModule(Module):
    prefix: str
    state: str = "off"
    def __init__(self, name: str, destination_modules: list[str]) -> None:
        super().__init__(name, destination_modules)
        self.prefix = "%"
    def __repr__(self) -> str:
        return self.prefix + super().__repr__()
    def receive_pulse(self, src: str, pulse: str):
        # print("FlipFlop:", src, "->", self.name, pulse)
        match(pulse, self.state):
            case ("H", _):
                return []
            case ("L", "off"):
                self.state = "on"
                return [(self.name, m, "H") for m in self.destination_modules]
            case ("L", "on"):
                self.state = "off"
                return [(self.name, m, "L") for m in self.destination_modules]

class ConjunctionModule(Module):
    memory: dict[str, str]
    def __init__(self, name: str, destination_modules: list[str]) -> None:
        super().__init__(name, destination_modules)
        self.memory = {}
        self.prefix = "&"
    def __repr__(self) -> str:
        return self.prefix + super().__repr__() + " ::: " + self.memory.__repr__()
    def initialize_memory(self, inputs: list[str]):
        for i in inputs:
            self.memory[i] = "L"
    def receive_pulse(self, src: str, pulse: str):
        # print("Conjunction:", src, "->",self.name, pulse)
        self.memory[src] = pulse
        all_high = all([p == "H" for p in self.memory.values()])
        send_pulse = "L" if all_high else "H"
        return [(self.name, m, send_pulse) for m in self.destination_modules]


def lines_to_modules(lines: list[str]):
    modules = {}
    inputs = {}
    for line in lines:
        module, destinations = line.split(" -> ")
        name = module[1:len(module)]
        dest_modules = destinations.split(", ")
        if module.startswith("%"):
            modules[name] = FlipFlopModule(name, dest_modules)
        elif module.startswith("&"):
            modules[name] = ConjunctionModule(name, dest_modules)
        elif module == "broadcaster":
            modules[module] = BroadcasterModule(module, dest_modules)
        else:
            raise ValueError("Invalid module: ", module)

        for dm in dest_modules:
            mname = name if (module.startswith("%") or module.startswith("&")) else module
            inputs[dm] = inputs.get(dm, [])
            inputs[dm].append(mname) 

    for i in inputs:
        match modules.get(i):
            case ConjunctionModule():
                modules[i].initialize_memory(inputs[i])
            case _:
                pass

    return modules


def push_button(modules: dict[str, Module]):
    queue = [(None, "broadcaster", "L")]

    pulses = {"H": 0, "L": 0}

    sent_rx = False

    while len(queue) > 0:
        src, module, pulse = queue.pop(0)
        pulses[pulse] = pulses[pulse] + 1
        if module not in modules:
            print("Unknown module", module)
            modules[module] = Module(module, [])
        next_modules = modules[module].receive_pulse(src, pulse)
        queue.extend(next_modules)
        if (module, pulse) == ("rx", "L"):
            sent_rx = True


    return (pulses, sent_rx)


def add_pulses(s: dict[str, int], pulse: dict[str, int]):
    return {
        "H": s["H"] + pulse["H"],
        "L": s["L"] + pulse["L"]
    }

def part1():
    lines = util.get_lines(input_str)
    modules = lines_to_modules(lines)
    sum_pulses = {"H":0, "L":0}
    for i in range(0, 1000):
        res, _ = push_button(modules)
        sum_pulses = add_pulses(sum_pulses, res)

    print(sum_pulses)
    return sum_pulses["H"] * sum_pulses["L"]


def part2():
    lines = util.get_lines(input_str)
    modules = lines_to_modules(lines)
    sum_pulses = {"H":0, "L":0}
    # for i in range(0, 1000):
    #     sum_pulses = add_pulses(sum_pulses, push_button(modules))
    while True:
        res, rx = push_button(modules)
        sum_pulses = add_pulses(sum_pulses, res)
        if rx == True:
            break

    print(sum_pulses)
    return sum_pulses["H"] * sum_pulses["L"]


print("Part 1", part1())
print("Part 2", part2())
