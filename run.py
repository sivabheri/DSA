def evaluate(gate_type, input1, input2):
    if gate_type == "AND":
        return input1 & input2
    elif gate_type == "OR":
        return input1 | input2
    elif gate_type == "NAND":
        return 1 - (input1 & input2)
    elif gate_type == "NOR":
        return 1 - (input1 | input2)
    elif gate_type == "XOR":
        return input1 ^ input2
    else:
        raise ValueError("Unknown gate type")

def simulate_circuit(n, gates, t, inputs, output_gate):
    gate_outputs = {gate: [0] * t for gate in gates}
    
    variables = {var: values for var, values in inputs.items()}
    
    for cycle in range(1, t):
        for gate, (gate_type, input1, input2) in gates.items():
            val1 = variables[input1][cycle - 1] if input1 in variables else gate_outputs[input1][cycle - 1]
            val2 = variables[input2][cycle - 1] if input2 in variables else gate_outputs[input2][cycle - 1]
            
            gate_outputs[gate][cycle] = evaluate(gate_type, val1, val2)
    
    return gate_outputs[output_gate]

n = int(input())
gates = {}
for _ in range(n):
    line = input().strip()
    output, expr = line.split('=')
    gate_type, inputs = expr.split('(')
    input1, input2 = inputs.strip(')').split(', ')
    gates[output.strip()] = (gate_type.strip(), input1.strip(), input2.strip())

t = int(input())
inputs = {}
for _ in range(len(gates) + 1):
    line = input().split()
    inputs[line[0]] = list(map(int, line[1:]))

output_gate = input().strip()
result = simulate_circuit(n, gates, t, inputs, output_gate)
print(' '.join(map(str, result)))
