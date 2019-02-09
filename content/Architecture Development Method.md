Title: Architecture Development Method - ADM
Date: 2019-02-09 10:20
Modified: 2019-02-09 19:30
Category: Enterprise Architecture
Tags: TOGAF, Enterprise Architecture
Slug: Architecture Development Method - ADM
Authors: Gonzalo Saenz
Status: published
Summary: This post is an introduction to TOGAF Architecture Development Method (ADM).


This post is an introduction to TOGAF Architecture Development Method (ADM).

The TOGAF ADM is the result of continuous contributions from a large number of architecture practitioners. It describes a method for developing and managing the lifecycle of an Enterprise Architecture, and forms the core of the TOGAF standard.

The application of the TOGAF ADM is supported by an extended set of resources, guidelines, templates, checklists, and other detailed materials. These resources can found in:

* Part III: ADM Guidelines & Techniques
* White Papers and Guides published by The Open Group, classified and referenced in the TOGAF Library

Some key points to understand ADM:

* The ADM is iterative. For each Iteration architects decide, breadth, level of detail, architectural assets to be leveraged.
* As a generic method it may be, tailored to specific needs.

Architecture Development Method is graphically represented with this diagram,
![ADM][]

In this post I will summarize the different ADM phases:

* [Preliminary Phase](#preliminary)
* [A) Architecture Vision](#vision)
* [B)Business Architecture](#business)
* [C) Information Systems Architecture](#information)
* [D) Technology Architecture](#technology)
* [E) Opportunities & Solutions](#opportunities)
* [F) Migration Planning](#migration)
* [G) Implementation Governance](#governance)
* [H) Architecture Change Management](#change)
* [Requirements Management](#requirements)

# ADM Guidelines and techniques

TOGAF ADM is not just a methodology, it comes with full feature set of guidelines and tehcniques to apply in the architecture development cycle.

Guidelines included in TOGAF Part III include:

* Applying Iteration to the ADM
* Applying the ADM across the Architecture Landscape

In a future post I will discuss in more details TOGAF Part III "ADM Guidelines and Techniques".

# Architecture Development Method

In a nutshell the ADM:

* ADM consists of phases
* ADM can be followed sequentially, but usually there are [iterations](#iterations), for example multiple iteration within phases B, C, D, or F & G. There are “standard” iterations defined in the standard.

Each phase consists of:

* Inputs

    - Organization/Industry context, external/internal regulations, Architecture repository, previous phases

* Steps
* Techniques
* Output

    - Architecture repository, Deliverables, artifacts, views, viewpoints

![ADM layers][adm_layers]

## ADM Iterations <a name="iterations"></a>

The suggested ADM iterations are displayed in the image below

![ADM Iterations][adm_iterations]


* **Architecture Capability** iterations support the creation1 and evolution of the required Architecture Capability

    This includes the initial mobilization of the architecture activity for a given purpose or architecture engagement type by establishing or adjusting the architecture approach, principles, scope, vision, and governance.

* **Architecture Development** iterations allow the creation of architecture content by cycling through, or integrating, Business, Information Systems, and Technology Architecture phases

    These iterations ensure that the architecture is considered as a whole. In this type of iteration stakeholder reviews are typically broader. As the iterations converge on a target, extensions into the Opportunities & Solutions and Migration Planning phases ensure that the architecture's implementability is considered as the architecture is finalized.

* **Transition Planning** iterations support the creation of formal change roadmaps for a defined architecture

* **Architecture Governance** iterations support governance of change activity progressing towards a defined Target Architecture

# ADM – Preliminary Phase <a name="preliminary"></a>

Preliminary phase is about defining “where, what, why, who, and how” enterprise architecture will be done in the enterprise.

Preliminary phase creates the conditions and context for an architecture capability. Failing to create conditions and context appropriate to your organization is a failure pattern.

Preliminary phase objectives:

* Determine architecture capability desired by the organization
    - organization context,
    - scope,
    - methods & processes,
    - maturity target.

* Establish the capability
    - establish organization model,
    - governance processes,
    - principles

# ADM – A) Architecture Vision <a name="vision"></a>

Architecture Vision objectives

* Defines the scope of the architecture development
* Identifies stakeholders
* Creates the Architecture Vision
* Secures approval to proceed

**Architecture Vision**, is a succinct description of the Target Architecture that describes its business value and the changes to the enterprise that will result from its successful deployment.

It serves as an aspirational vision and a boundary for detailed architecture development.

# ADM – Enterprise Architecture Development

Three phases of The TOGAF ADM result in the development of the Enterprise Architecture

* Phase B: Business Architecture
* Phase C: Information Systems Architectures
* Phase D: Technology Architecture

In TOGAF 9, these phases are described in a consistent manner in terms of:

* Approach
* Inputs
* Steps .. The same for each phase
    - Techniques within each phase are different
* Outputs

## Enterprise Architecture Development Steps

1. Select Reference Models, Viewpoints and Tools
2. Develop Baseline
3. Architecture Description
4. Develop Target
5. Architecture Description
6. Perform Gap Analysis
7. Define Candidate Roadmap Components
8. Resolve Impacts across the
9. Architecture Landscape
10. Conduct Formal Stakeholder Review
11. Finalize the Architecture
12. Create Architecture Definition Document

# ADM – B) Business Architecture <a name="business"></a>

Business Architecture is a description of the structure and interaction between the business strategy, organization, functions, business processes, and information needs.

** Phase B : Business Architecture - Objectives**

* Develop Target Business Architecture
    * How the enterprise needs to operate
    * To achieve business goals
    * To respond to strategic drivers
    * Set out in the Architecture Vision
    * Addresses Statement of Architecture Work and stakeholder concerns
* Identify candidate Architecture Roadmap components, based on gaps between Baseline and Target Business Architectures

# ADM – C) Information Systems Architecture <a name="information"></a>

** Phase C : Overall - Objectives**

* Develop Target Information Systems (Data and Application) Architectures
    * Enable the Business Architecture and Architecture Vision
    * Addresses Statement of Architecture Work and Stakeholder Concerns
* Identify candidate Architecture Roadmap components
    * Based on gaps between Baseline and Target Information Systems Architectures

Phase C : ** Approach – Data or Application Driven?**
* Phase C involves some combination of Data and Application Architecture, in either order.
    * Data driven approach when data drives choice of applications
    * Application driven approach when large applications dominate your core business, For example ERP and CRM
* In practice these two architectures must be mutually supportive and consistent

# ADM – D) Technology Architecture <a name="technology"></a>

Technology Architecture is a description of the structure and interaction of the platform services, and logical and physical technology components.

** Phase D : Technology Architecture - Objectives**

* Develop Target Technology Architecture
    * Enable the Logical and Physical Application and Data components and Architecture Vision
    * Address Statement of Architecture Work and Stakeholder Concerns
* Identify candidate Architecture Roadmap components
Based on gaps between Baseline and Target Technology Architectures

# ADM – E) Opportunities & Solutions <a name="opportunities"></a>

This phase describes the first phase of the ADM which is directly concerned with implementation, identifying major work packages to be undertaken and creating a migration strategy

** Phase E - Opportunities and Solutions - Objectives**

* Generate the initial complete version of Architecture Roadmap based on outputs from Phases B, C and D
    * Gap analysis
    * Candidate Architecture Roadmap components
* Determine whether incremental approach is required. If so, identify Transition Architectures that will deliver continuous business value

Stakeholder requirements drive the architecture focus and decision making.

# ADM – F) Migration Planning <a name="migration"></a>

This phase describes the creation of a viable Implementation and Migration Plan in co-operation with the portfolio and project managers

** Phase F - Migration Planning - Objectives**

* Finalize Architecture Roadmap and supporting Implementation and Migration Plan
* Ensure that Implementation and Migration Plan is coordinated with the enterprise’s approach to managing and implementing change in enterprise’s overall change portfolio
* Endure that business value and cost of work packages and Transition Architectures is understood by key stakeholders

# ADM – G) Implementation Governance <a name="governance"></a>

This module addresses the role of the architecture team during the implementation phase of the project

**Phase G - Implementation Governance - Objectives**

* Ensure conformance with Target Architecture by implementation projects
* Perform appropriate governance functions for solution and any implementation-driven architecture Change Requests

# ADM – H) Architecture Change Management <a name="change"></a>

This phase establishes procedures for managing change to the architecture landscape, the architecture capability and operating all architecture governance processes throughout the lifetime of the Architecture.

**Phase H - Architecture Change Management - Objectives**

* Ensure that architecture lifecycle is maintained
* Ensure that the Architecture Governance Framework is executed
* Ensure that the Enterprise Architecture Capability meets current requirements

* Change Management: Supports implemented architecture as a dynamic architecture, examples
    * Architecture continues to fit but the solutions may not
    * Systems deteriorate and require upgrades and modifications
    * Operational context requires more scalability than solutions can deliver
* Provides flexibility to enable the architecture to evolve rapidly to changes in the business and technology environments, for example
    - Monitoring business growth and decline
* Leverages performance management and reporting capability of the work products to ensure effectiveness of the architecture
* Maximising business value with a steady state Business Architecture requires continually assessments to ensure that the value is achieved.

# ADM – Requirements Management <a name="requirements"></a>

ADM Requirements Management describes the steps taken during the continuous Requirements Management performed throughout the ADM cycle

** Architecture Requirements Management - Objectives**

* Ensure that the Requirements Management process is sustained and operates for all relevant ADM phases
* Manage architecture requirements identified during any execution of the ADM cycle or a phase
* Ensure that relevant architecture requirements are available for use by each phase as the phase is executed

# Reference

You can find more information in [The Open Group][open_group] website. Specially in TOGAF "Part II - Architecture Development Method" and Part III "ADM Guidelines and Techniques"

# Conclussion

The TOGAF ADM defines a recommended sequence for the various phases and steps involved in developing an architecture, but it cannot recommend a scope - this has to be determined by the organization itself, bearing in mind that the recommended sequence of development in the ADM process is an iterative one, with the depth and breadth of scope and deliverables increasing with each iteration. Each iteration will add resources to the organization's Architecture Repository.

The main guideline is to focus on what creates value to the enterprise, and to select horizontal and vertical scope, and time periods, accordingly. Whether or not this is the first time around, understand that this exercise will be repeated, and that future iterations will build on what is being created in the current effort, adding greater width and depth.

In future posts I will cover in more details each phase of ADM.

That's all folks!

Gonzalo Sáenz


<!-- Links -->

[adm_iterations]: /images/ADM_iterations.png "ADM Iterations"
[open_group]: http://pubs.opengroup.org/architecture/togaf92-doc/arch/index.html "TOGAF - The Open Group"
[adm_layers]: /images/TOGAF_ADM_layers.png "TOGAF ADM layers"
[ADM]: /images/ADM.png "Architecture Development Method"
