import csv


def export_to_file(idx, lattice, output_dir=None):
    if output_dir is None:
        output_dir = "./"
    if not output_dir.endswith("/"):
        output_dir += "/"

    hasse_lattice, concepts = lattice.hasse, lattice.concepts
    with open(f'{idx}_hasse.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        for l in hasse_lattice:
            writer.writerow(l)

    with open(f'{idx}_concepts_by_id.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        for c in concepts:
            str_c = str(c)
            idx = str_c.index('],')
            str_1, str_2 = str_c[1:idx + 1], str_c[idx + 2:-1]
            writer.writerow([f'{c.hr_O()}', f'{c.hr_A()}'])
