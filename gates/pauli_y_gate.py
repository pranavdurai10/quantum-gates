'''
///////////////////////////////////////////////////////////////////////////
Code written by Pranav Durai for Quantum Computers on 28.05.2023 @ 20:22:15

Component: Pauli-Y-Gate (bit-flip-gate)

Framework: Qiskit 0.43.0
///////////////////////////////////////////////////////////////////////////
'''

# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1)

# Apply Pauli-Y gate to the qubit
circuit.y(0)

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