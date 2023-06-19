'''
///////////////////////////////////////////////////////////////////////////
Code written by Pranav Durai for Quantum Computer on 29.05.2023 @ 22:57:01

Component: Pauli-Z-Gate (bit-flip-gate)

Framework: Qiskit 0.43.0
///////////////////////////////////////////////////////////////////////////
'''

# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1)

# Apply Pauli-Z gate to the qubit
circuit.z(0)

# Measure the qubit
circuit.measure_all()

# Simulate the circuit using the local Aer simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1)

# Get the result
result = job.result()
counts = result.get_counts(circuit)

# Print the measurement outcome
print("Measurement outcome:", list(counts.keys())[0])
