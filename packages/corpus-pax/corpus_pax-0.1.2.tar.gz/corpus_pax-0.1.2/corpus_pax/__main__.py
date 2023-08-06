from sqlpyd import Connection

from .entities import Individual, Org, OrgMember


def init_person_tables(c: Connection) -> Connection:
    """Create tables related to persons, i.e. individuals and organizations."""

    # creates tables
    c.create_table(Individual)
    c.create_table(Org)
    c.create_table(OrgMember)

    # auto-generate indexes on fks
    c.db.index_foreign_keys()

    # add a trigger
    OrgMember.on_insert_add_member_id(c)
    return c


def add_individuals_from_api(c: Connection, replace_img: bool = False):
    """Add records of individuals from an API call."""
    for member in Individual.list_members_repo():
        Individual.make(c, member["url"], replace_img)


def add_organization_from_api(c: Connection, replace_img: bool = False):
    """Add records of organizations from an API call."""
    for member in Org.list_orgs_repo():
        Org.make(c, member["url"], replace_img)


def init_persons(c: Connection, replace_img: bool = False):
    """Creates the tables and populates the same."""
    init_person_tables(c)
    add_individuals_from_api(c, replace_img)
    add_organization_from_api(c, replace_img)
