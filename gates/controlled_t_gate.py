'''
///////////////////////////////////////////////////////////////////////////
Code written by Pranav Durai for Quantum Computers on 11.06.2023 @ 18:00:01

Component: Controlled-T Gate

Framework: Qiskit 0.43.0
///////////////////////////////////////////////////////////////////////////
'''

# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
circuit = QuantumCircuit(2)

# Apply the Controlled-T gate using a combination of gates
circuit.h(1)
circuit.cx(0, 1)
circuit.tdg(1)
circuit.cx(0, 1)
circuit.t(1)
circuit.cx(0, 1)

# Measure the qubits
circuit.measure_all()

# Simulate the circuit using the local Aer simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1)

# Get the result
result = job.result()
counts = result.get_counts(circuit)

# Print the measurement outcome
print("Measurement outcome:", list(counts.keys())[0])