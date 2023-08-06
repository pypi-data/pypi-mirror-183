from chemcloud import CCClient
from chemcloud.models import AtomicInput, Molecule

client = CCClient()

water = Molecule.from_data("pubchem:water")

atomic_input = AtomicInput(
    molecule=water,
    driver="energy",
    model={
        "method": "GFN2-xTB",
    },
    keywords={
        "accuracy": 1.0,
        "max_iterations": 50,
    },
)


future_result = client.compute(atomic_input, engine="xtb")
result = future_result.get()
# AtomicResult object containing all returned data
print(result)
# The energy value requested
print(result.return_result)
print(result.provenance.wall_time)
