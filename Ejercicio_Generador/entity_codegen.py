"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'person.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    # Create output folder
    srcgen_folder = join(this_folder, 'output')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity


    # Load template
    template = jinja_env.get_template('reporte.template')


    for entity in person_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%s.html" % entity.name.capitalize()), 'w') as f:
            x = template.render(entity=entity)
            f.write(x.encode('utf-8'))


    cssTemplate = jinja_env.get_template('myStyle.template')
    with open(join(srcgen_folder,
                       "%s.css" % "myStyle"), 'w') as f:
            f.write(cssTemplate.render())


if __name__ == "__main__":
    main()
