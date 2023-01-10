from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    CheckConstraint,
    select,
    insert,
    update,
    delete,
)

from components.db_conection import DATABASE, engie

# from db_conection import DATABASE,engie


class Tecnico(DATABASE):
    """Clase que contiene la estructura de el tecnico
    y tambien permite realizar el mapeo de clase a entidad
    relacion por medio de sqlalchemy

    Args:
        DATABASE (DATABASE): estructura que permite heradar los 
        atributos para generar el mapeo a la bd
    """
    __tablename__ = "tecnico"
    id = Column(String(20), primary_key=True)
    nombre = Column(String(20), nullable=False)
    sueldo = Column(Integer, nullable=False)
    sucursal_id = Column(String(20), ForeignKey("sucursal.id"))

    def get_all():       
        query = """
            SELECT t.id , t.nombre ,t.sueldo,s.nombre as sucursal 
            FROM test.tecnico t inner join test.sucursal s on  t.sucursal_id =  s.id       
        """
        with engie.connect() as connection:
            result = connection.execute(query)
            print(result)
            connection.close()

        return result.all()

    def instert(tecnico):
        with engie.connect() as connection:
            try:
                connection.execute(
                    insert(Tecnico).values(
                        id=tecnico["id"],
                        nombre=tecnico["nombre"],
                        sueldo=tecnico["sueldo"],
                        sucursal_id=tecnico["sucursal_id"],
                    )
                )
                for elemento_id, cantidad in tecnico["elementos"].items():
                    connection.execute(
                        insert(ElementoXTecnico).values(
                            elemento_id=elemento_id,
                            tecnico_id=tecnico["id"],
                            cantidad=cantidad,
                        )
                    )
                connection.close()
            except Exception as err:
                return err
        return "ok"

    def update(tecnico):
        try:
            with engie.connect() as connection:
                connection.execute(
                    update(Tecnico)
                    .where(Tecnico.id == tecnico["id"])
                    .values(
                        nombre=tecnico["nombre"],
                        sueldo=tecnico["sueldo"],
                        sucursal_id=tecnico["sucursal_id"],
                    )
                )
                for elemento_id, cantidad in tecnico["elementos"].items():
                    connection.execute(
                        update(ElementoXTecnico)
                        .where(
                            ElementoXTecnico.elemento_id == elemento_id
                            and ElementoXTecnico.tecnico_id == tecnico["id"]
                        )
                        .values(cantidad=cantidad)
                    )
                connection.close()
        except Exception as err:
            return err
        return "ok"

    def delete(tecnico):

        with engie.connect() as connection:
            connection.execute(
                delete(ElementoXTecnico).where(
                    ElementoXTecnico.tecnico_id == tecnico["id"]
                )
            )
            connection.execute(delete(Tecnico).where(Tecnico.id == tecnico["id"]))
            connection.close()
    def get_elementos(tecnico):
        id =  tecnico["id"]
        query = """
            select t.id,et.cantidad,e.id, e.nombre, e.descripcion from test.tecnico t 
            inner join test.elementoxtecnico et on t.id = et.tecnico_id
            inner join test.elemento e on et.elemento_id =  e.id
            where t.id = '{}';""".format(str(id))
        with engie.connect() as connection:
            result = connection.execute(query)
            print(result)
            connection.close()

        return result.all()


class Sucursal(DATABASE):
    __tablename__ = "sucursal"
    id = Column(String(20), primary_key=True)
    nombre = Column(String(20), unique=True, nullable=False)
    def get_all():
        query = """
            SELECT *
            FROM test.sucursal s     
        """
        with engie.connect() as connection:
            result = connection.execute(query)
            print(result)
            connection.close()

        return result.all()


class Elemento(DATABASE):
    __tablename__ = "elemento"
    id = Column(String(20), primary_key=True)
    nombre = Column(String(20), unique=True, nullable=False)
    descripcion = Column(String(20), nullable=False)


class ElementoXTecnico(DATABASE):
    """clase que tiene la informacion de los elemenotos 
    que va a tener cada tecnico y su correspondeiente cantidad

    Args:
        DATABASE (_type_): _description_
    """
    __tablename__ = "elementoxtecnico"
    elemento_id = Column(String(20), ForeignKey("elemento.id"), primary_key=True)
    tecnico_id = Column(String(20), ForeignKey("tecnico.id"), primary_key=True)
    cantidad = Column(
        Integer, CheckConstraint("cantidad between 1 and 10"), nullable=False
    )


# DATABASE.metadata.create_all(engie)
