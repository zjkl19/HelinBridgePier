# -*- coding: utf-8 -*-
# -*- coding: mbcs -*-

#comment by lindinan

from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()        
       
session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

bottomPartName='Part-1'
middlePartName='Part-2'
upperPartName='Part-3'
meshSize=0.4

# Create a model
modelName='HeLinBridgePartial'
mdb.Model(name=modelName)

#create material
mdb.models[modelName].Material(name='C30')
mdb.models[modelName].materials['C30'].Density(table=((2549.0, ), ))
mdb.models[modelName].materials['C30'].Elastic(table=((3.0e10, 0.2), ))
#create section
mdb.models[modelName].HomogeneousSolidSection(name='Section-1',material='C30', thickness=None)



#bottom part
s1 = mdb.models[modelName].ConstrainedSketch(name='__profile__',sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.Line(point1=(-2.0, 0.0), point2=(2.0, 0.0))
s1.Line(point1=(2.0, 0.0), point2=(2.0, 3.74))
s1.Line(point1=(2.0, 3.74), point2=(4.13, 4.74))
s1.Line(point1=(4.13, 4.74), point2=(-4.13, 4.74))
s1.Line(point1=(-4.13, 4.74), point2=(-2.0, 3.74))
s1.Line(point1=(-2.0, 3.74), point2=(-2.0, 0.0))
p = mdb.models[modelName].Part(name=bottomPartName, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models[modelName].parts[bottomPartName]
p.BaseSolidExtrude(sketch=s1, depth=1.8)

#middle part
s = mdb.models[modelName].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.Line(point1=(-0.9, 0.0), point2=(0.9, 0.0))
s.Line(point1=(0.9, 0.0), point2=(6.0, 1.5))
s.Line(point1=(6.0, 1.5), point2=(-6.0, 1.5))
s.Line(point1=(-6.0, 1.5), point2=(-0.9, 0.0))
p = mdb.models[modelName].Part(name=middlePartName, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models[modelName].parts[middlePartName]
p.BaseSolidExtrude(sketch=s, depth=16.52)

#upper part
s1 = mdb.models[modelName].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.Line(point1=(-8.26, 0.0), point2=(8.26, 0.0))
s1.Line(point1=(8.26, 0.0), point2=(8.26, 0.65))
s1.Line(point1=(8.26, 0.65), point2=(8.89, 0.8))
s1.Line(point1=(8.89, 0.8), point2=(8.89, 0.9))
s1.Line(point1=(8.89, 0.9), point2=(-8.89, 0.9))
s1.Line(point1=(-8.89, 0.9), point2=(-8.89, 0.8))
s1.Line(point1=(-8.89, 0.8), point2=(-8.26, 0.65))
s1.Line(point1=(-8.26, 0.65), point2=(-8.26, 0.0))
p = mdb.models[modelName].Part(name=upperPartName, dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models[modelName].parts[upperPartName]
p.BaseSolidExtrude(sketch=s1, depth=12.0)

#assign section
p = mdb.models[modelName].parts[bottomPartName]
c = p.cells
#cells = c.findAt(((-1.376667, 4.74, 1.2), ))
region = p.Set(cells=c, name='Set-1')
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p1 = mdb.models[modelName].parts[middlePartName]

p = mdb.models[modelName].parts[middlePartName]
c = p.cells
#cells = c.findAt(((0.3, 0.0, 11.013334), ))
region = p.Set(cells=c, name='Set-1')
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

p = mdb.models[modelName].parts[upperPartName]
c = p.cells
#cells = c.findAt(((-8.89, 0.833333, 8.0), ))
region = p.Set(cells=c, name='Set-1')
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

#create instance
a1 = mdb.models[modelName].rootAssembly
p = mdb.models[modelName].parts[bottomPartName]
a1.Instance(name='Part-1-1', part=p, dependent=OFF)
a1.Instance(name='Part-1-2', part=p, dependent=OFF)

p = mdb.models[modelName].parts['Part-2']
a1.Instance(name='Part-2-1', part=p, dependent=OFF)
p = mdb.models[modelName].parts['Part-3']
a1.Instance(name='Part-3-1', part=p, dependent=OFF)

#translate and rotate instance
a1 = mdb.models['HeLinBridgePartial'].rootAssembly
a1.translate(instanceList=('Part-1-1', ), vector=(4.13, 0.0, -0.9))
a1.translate(instanceList=('Part-1-2', ), vector=(-4.13, 0.0, -0.9))
a1.translate(instanceList=('Part-2-1', ), vector=(8.26, 4.74, 0.0))
a1.rotate(instanceList=('Part-2-1', ), axisPoint=(8.26, 4.74, 0.0), 
    axisDirection=(0.0, 1.5, 0.0), angle=-90.0)
a1.translate(instanceList=('Part-3-1', ), vector=(0.0, 6.24, -6.0))


a1.InstanceFromBooleanMerge(name='Part-All', instances=(
    a1.instances['Part-1-1'], a1.instances['Part-1-2'], 
    a1.instances['Part-2-1'], a1.instances['Part-3-1'], ), 
    originalInstances=SUPPRESS, domain=GEOMETRY)

a1.makeIndependent(instances=(a1.instances['Part-All-1'], ))

#can operate manually
a = mdb.models['HeLinBridgePartial'].rootAssembly
e1 = a.instances['Part-All-1'].edges
pickedEdges = e1.findAt(((8.89, 7.14, -3.0), ))
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.0567)
a = mdb.models['HeLinBridgePartial'].rootAssembly
pickedEdges = e1.findAt(((-8.89, 7.14, -3.0), ))
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.0567)
a = mdb.models['HeLinBridgePartial'].rootAssembly
pickedEdges = e1.findAt(((8.89, 7.14, -2.4897), ))
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.9399)
a = mdb.models['HeLinBridgePartial'].rootAssembly
pickedEdges = e1.findAt(((-8.89, 7.14, -2.4897), ))
a.PartitionEdgeByParam(edges=pickedEdges, parameter=0.9399)

f1 = a.instances['Part-All-1'].faces
pickedFaces = f1.findAt(((-2.963333, 7.14, 2.0), ))
v1 = a.instances['Part-All-1'].vertices
a.PartitionFaceByShortestPath(point1=v1.findAt(coordinates=(-8.89, 7.14, 
    5.319692)), point2=v1.findAt(coordinates=(8.89, 7.14, 5.319692)), 
    faces=pickedFaces)
f1 = a.instances['Part-All-1'].faces
pickedFaces = f1.findAt(((-2.963333, 7.14, 1.773261), ))
v11 = a.instances['Part-All-1'].vertices
a.PartitionFaceByShortestPath(point1=v11.findAt(coordinates=(-8.89, 7.14, 
    -5.3196)), point2=v11.findAt(coordinates=(8.89, 7.14, -5.3196)), 
    faces=pickedFaces)

#create step
mdb.models[modelName].StaticStep(name='Step-1', previous='Initial')

#create boundry condition
a = mdb.models[modelName].rootAssembly
f1 = a.instances['Part-All-1'].faces
faces1 = f1.findAt(((-3.463333, 0.0, 0.3), ), ((4.796667, 0.0, 0.3), ))
region = a.Set(faces=faces1, name='Set-1')
mdb.models[modelName].DisplacementBC(name='BC-1', 
    createStepName='Step-1', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
    fieldName='', localCsys=None)

#create load
mdb.models[modelName].Gravity(name='Load-Gravity', 
    createStepName='Step-1', comp2=-9.8, distributionType=UNIFORM, field='')

s1 = a.instances['Part-All-1'].faces
side1Faces1 = s1.findAt(((2.963333, 7.14, 5.546461), ))
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models[modelName].Pressure(name='Load-2200', 
    createStepName='Step-1', region=region, distributionType=TOTAL_FORCE, field='', 
    magnitude=2200.0e3, amplitude=UNSET)

s1 = a.instances['Part-All-1'].faces
side1Faces1 = s1.findAt(((-2.963333, 7.14, -5.5464), ))
region = a.Surface(side1Faces=side1Faces1, name='Surf-2')
mdb.models[modelName].Pressure(name='Load-2800', 
    createStepName='Step-1', region=region, distributionType=TOTAL_FORCE, field='', 
    magnitude=2800.0e3, amplitude=UNSET)


#should mesh manually
c1 = a.instances['Part-All-1'].cells
pickedCells = c1.findAt(((-3.463333, 0.0, 0.3), ))
e11 = a.instances['Part-All-1'].edges
v1 = a.instances['Part-All-1'].vertices
a.PartitionCellByPlaneNormalToEdge(edge=e11.findAt(coordinates=(8.26, 6.7275, 
    6.0)), point=v1.findAt(coordinates=(8.26, 6.24, 6.0)), cells=pickedCells)

c1 = a.instances['Part-All-1'].cells
pickedCells = c1.findAt(((-3.463333, 0.0, 0.3), ))
v11 = a.instances['Part-All-1'].vertices
a.PartitionCellByPlaneThreePoints(point1=v11.findAt(coordinates=(8.26, 4.74, 
    -0.9)), point2=v11.findAt(coordinates=(8.26, 4.74, 0.9)), 
    point3=v11.findAt(coordinates=(-8.26, 4.74, 0.9)), cells=pickedCells)

#create mesh
partInstances =(a.instances['Part-All-1'], )
a.seedPartInstance(regions=partInstances, size=meshSize, deviationFactor=0.1, 
    minSizeFactor=0.1)
a.generateMesh(regions=partInstances)

