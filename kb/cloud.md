---
title: Cloud Computing
---

Cloud computing services provide IT resources through the internet, including virtual machines and clusters
databases, storage, and access to LLMs (amongst many, many others). Some of the big cloud service providers are
[Amazon AWS](http://aws.amazon.com), [Google Cloud (GCP)](https://cloud.google.com), and [Microsoft Azure](https://azure.microsoft.com).

## SCF support

The information on this page may be useful in getting an overview of cloud resources for LLMs and accessing cloud resources through a Berkeley-based account via bCloud.

However, given the wide variety of services, complexity of the services and speed at which they change, we primarily recommend that Statistics affiliates reach out to us directly to talk about options for using cloud resources to support research or teaching.

## LLMs in the cloud

With regard to LLM/agent access, each cloud service has an LLM/agent service (Google Agent Platform, AWS Bedrock, Microsoft Foundry) that allows one to query LLMs hosted by the service. The services generally have agreements with some of the actual model providers (e.g., Anthropic for Claude models) in which the service hosts the models and handles authentication (either by a login process to your account on the cloud service or an API key/token). All queries go through the cloud service endpoint (a URL) rather than going directly to the model provider.

Note that access through the cloud service is distinct from pay-as-you go through an API key/token directly from the model provider and also distinct from paying for a subscription to an AI coding agent (such as Claude Code or Codex) through the coding agent provider. Such access is paid directly to the model/agent provider (e.g., by credit card) and cannot be done with a Berkeley chartstring. 

Finally note that at present Berkeley's agreement with Google only provides chat access to Google's Gemini models (at gemini.google.com and login with your CalNet credentials) and not access to Gemini Code Assist or API access to Gemini.

The SCF has [some additional overview of the cloud landscape around AI/LLMs](https://docs.google.com/document/d/1vf_ODinTH3LJAhrHPF89kyBYaif4-2ZifMC1h3Z-36o/edit?usp=sharing
) in an evolving document created in September 2026. 

## bCloud

Campus' [bCloud Public Cloud
Service](https://docs.google.com/presentation/d/1KyhdetJgjUI8eivoJn1HWaeuY7eKTRrmmn3D-txdg3o/edit#slide=id.gcfb890c19a_0_28)
can help researchers by providing UC discounts, centralized billing
(using a chartstring instead of a credit card), CalNet authentication,
and other methods of support. We encourage people to leverage this
service to ease various administrative burdens involved with using the
cloud. 

In particular, if a service is available through bCloud then it is generally best to use that approach so as to pay by chartstringm as campus discourages (and in some cases prevents) reimbursement for expenses paid by credit card.

The initial steps are: 

1. Determine which cloud service you want to use based on their offerings.
2. Apply for a bCloud Public Cloud Account specific to the cloud service of interest (GCP, AWS, or Azure).

Once you have access to your bCloud account on the service, you can use the service's console (a web-based GUI) or command-line interface (CLI).

The SCF is happy to provide assistance with using the cloud services (including setting up a bCloud Public Cloud Account).

