# weather-collector

# Why?

There is a need to collect data from weather APIs to improve the Digital Core to regulate the display brightness

# What?

Is a simple module to handle various weather endpoints or endpoints in general

![](Endpoints.png)

## Usage

The idea is to provide a simple interface for handling collections of APIs. Through time, the objects should become
very abstract to be reusable in different environments. This is the moment a package shoudl be factored out, either
through a framework or just a package.

Basically, your use case should implement the following interfaces

* endpoints.interface
* endpoint_collection.interface
* sampler.interface (optional)

## Documentation of the Endpoints

<https://docs.tomorrow.io/reference/post-route>

## Delimiter

Timestamp1, timestamp2, wert1 , wert2, durchschnitt;
