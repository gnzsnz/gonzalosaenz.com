Title: Example Viewpoints
Date: 2021-02-13 10:08
Modified: 2010-02-13 10:08
Category: Enterprise Architecture
Tags: Enterprise Architecture, Archimate
Slug: Example Viewpoints
Authors: Gonzalo Sáenz
Summary: Example Viewpoints
Status: published

# Example Viewpoints

## Basic Viewpoints in the ArchiMate Language

A viewpoint in the ArchiMate language is a selection of a relevant subset of the ArchiMate elements and their relationships. This is the representation of that part of an architecture that is expressed in different diagrams.

The most basic type of viewpoint is a simple selection of a relevant subset of the ArchiMate concepts and the representation of that part of an architecture that is expressed in this selection, geared towards the stakeholders that will use the resulting views.

The different viewpoints are grouped into categories that indicate which direction and which elements the viewpoint is looking at:

1. *Composition*: viewpoints that define internal compositions and aggregations of elements.

2. *Support*: viewpoints where you are looking at elements that are supported by other elements, typically from one layer and upwards to an above layer.

3. *Cooperation*: towards peer elements which cooperate with each other, typically across aspects.

4. *Realization*: viewpoints where you are looking at elements that realize other elements, typically from one layer and downwards to a below layer.

| Category: Composition         |                                                              |                                    |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------- |
| Name                          | Perspective                                                  | Scope                              |
| Organization                  | Structure of the enterprise in terms of roles,  departments, etc. | Single layer, single aspect        |
| Application Structure         | Shows the structure of a typical  application in terms of its constituents. | Single layer, multiple aspect      |
| Information Structure         | Shows the structure of the information  used in the enterprise. | Multiple layer, single aspect      |
| Technology                    | Infrastructure and platforms underlying  the enterprise’s information systems in terms of networks, devices, and  system software. | Single layer, multiple aspect      |
| Layered                       | Provides overview of architecture(s).                        | Multiple layer, multiple aspect    |
| Physical                      | Physical environment and how this relates  to IT infrastructure. | Multiple layer, multiple aspect    |
| Category: Support             |                                                              |                                    |
| Name                          | Perspective                                                  | Scope                              |
| Product                       | Shows the contents of products.                              | Multiple layer, multiple aspect    |
| Application Usage             | Relates applications to their use in, for  example, business processes. | Multiple layer, multiple aspect    |
| Technology Usage              | Shows how technology is used by  applications.               | Multiple layer, multiple aspect    |
| Category: Cooperation         |                                                              |                                    |
| Name                          | Perspective                                                  | Scope                              |
| Business Process Cooperation  | Shows the relationships between various  business processes. | Multiple layer, multiple aspect    |
| Application Cooperation       | Shows application components and their  mutual relationships. | Application layer, multiple aspect |
| Category:  Realization        |                                                              |                                    |
| Name                          | Perspective                                                  | Scope                              |
| Service Realization           | Shows how services are realized by the  requisite behavior.  | Multiple layer, multiple aspect    |
| Implementation and Deployment | Shows how applications are mapped onto  the underlying technology. | Multiple layer, multiple aspect    |
