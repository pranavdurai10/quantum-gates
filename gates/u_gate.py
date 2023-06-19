'''
///////////////////////////////////////////////////////////////////////////
Code written by Pranav Durai for Quantum Computer on 18.06.2023 @ 22:29:12

Component: U1, U2, U3 Gates

Framework: Qiskit 0.43.0
///////////////////////////////////////////////////////////////////////////
'''

# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1)

# Apply the U1 gate
theta = 0.3  # Parameter for U1 gate
circuit.u1(theta, 0)

# Apply the U2 gate
phi = 0.4  # Parameter for U2 gate
lambda_ = 0.5  # Parameter for U2 gate
circuit.u2(phi, lambda_, 0)

# Apply the U3 gate
theta_ = 0.2  # Parameter for U3 gate
phi_ = 0.6  # Parameter for U3 gate
lambda_ = 0.7  # Parameter for U3 gate
circuit.u3(theta_, phi_, lambda_, 0)

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