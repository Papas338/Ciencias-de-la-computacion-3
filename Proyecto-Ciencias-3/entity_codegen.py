"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build restaurant model from libreria.ent file
    libreria_model = entity_mm.model_from_file(join(this_folder, 'libreria.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in libreria_model.entities:
            return True
        else:
            return False

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int',
                'string': 'String'
                #'bool': 'boolean'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javatype'] = javatype

    # Load template
    template = jinja_env.get_template('clase.template')

    for entity in libreria_model.entities:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%s.java" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))
    # Load template
    template = jinja_env.get_template('estilo.template')

    for entity in libreria_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "estilo%s.css" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))
     # Load template
    template = jinja_env.get_template('home.template')

    for entity in libreria_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "home%s.html" % entity.name.capitalize()), 'w') as f:
            
            x = template.render(entity=entity)
            f.write(x.encode('utf-8'))

    # Load template
    template = jinja_env.get_template('busqueda.template')

    for entity in libreria_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "busqueda%s.php" % entity.name.capitalize()), 'w') as f:
            x = template.render(entity=entity)
            f.write(x.encode('utf-8'))

if __name__ == "__main__":
    main()