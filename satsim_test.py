from satsim import gen_multi, load_json
import satsim
# load a template json file``
ssp = load_json('input/London_ISS_radec.json')

# generate files
gen_multi(ssp, eager=True, output_dir='output/')