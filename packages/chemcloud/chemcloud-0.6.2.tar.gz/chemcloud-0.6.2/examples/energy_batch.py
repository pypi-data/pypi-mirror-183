from chemcloud import CCClient
from chemcloud.models import AtomicInput, Molecule

client = CCClient()

water = Molecule.from_data("pubchem:water")

atomic_input = AtomicInput(
    molecule=water,
    model={"method": "B3LYP", "basis": "6-31g"},
    driver="energy",
    keywords={
        "closed": True,
        "restricted": True,
    },
)

future_result = client.compute([atomic_input] * 2, engine="terachem_fe")
result = future_result.get()
# Array of AtomicResult objects
print(result)
