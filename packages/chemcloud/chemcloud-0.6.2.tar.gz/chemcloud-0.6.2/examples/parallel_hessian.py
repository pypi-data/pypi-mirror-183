from chemcloud import CCClient
from chemcloud.models import AtomicInput, Molecule

client = CCClient()

water = Molecule.from_data("pubchem:water")

# Hessian computation
atomic_input = AtomicInput(
    molecule=water,
    model={"method": "B3LYP", "basis": "6-31g"},
    driver="hessian",
    extras={
        "bigchem:keywords": {
            "dh": 5e-3,  # OPTIONAL: displacement for finite difference
        },
    },
)
future_result = client.compute(atomic_input, engine="bigchem")
result = future_result.get()
# AtomicResult object containing all returned data
print(result)
# The hessian matrix
print(result.return_result)
