'''
///////////////////////////////////////////////////////////////////////////
Code written by Pranav Durai for Quantum Computers on 31.05.2023 @ 21:26:45

Component: Controlled-NOT Gate (CNOT) 

Framework: Qiskit 0.43.0
///////////////////////////////////////////////////////////////////////////
'''

# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with two qubits
circuit = QuantumCircuit(2)

# Apply the CNOT gate with control qubit 0 and target qubit 1
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