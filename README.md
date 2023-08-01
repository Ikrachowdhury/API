  
# Learning API

This is a simple project for learning and creating basic Rest-API
---

## Technologies Used
 * python
 * flask
 * flask_restful
 * SQLAlchemy
 ---

## Learning Agenda
* *What is API*<br>
      API stands for Application Programming Interface. API Can be thought as the middle man between two applications to transfer data to one another. For example, if an application wants some location data/map for its work it can get the location data/map from google map through using google map API. This Google map Api is the gateway interface for these two applications to request data and get data.
* *Type of API*
  1. WEB
  2. Rest
  3. SOAP
* *REST API*<br>
      A RESTful API is an architectural style for an application program interface API that uses HTTP requests to access and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the reading, updating, creating and deleting of operations concerning resources.
* *Architectural Constraints of RESTful API*
  1. **Client - Server**:
     * Client who requests for the resources.
     * Server who has the resources
  3. **Uniform Interface**: It is a key constraint that differentiate between a REST API and Non-REST API. It suggests that there should be a uniform way of interacting with a given server irrespective of device or type of application (Website, Mobile app)
  4. **Stateless**: It means that the necessary state to handle the request is contained within the request itself and  server or do not store anything related to the session.
  5. **Cacheable**: Every response should include whether the response is cacheable or not and for how much duration responses can be cached at the client side. client will return the data from its cache for any subsequent request and there would be no need to send the request again to the server.
  6. **Layered System**: An application architecture needs to be composed of multiple layers. Each layer does not know anything about any layer other than that of the immediate layer and there can be a lot of intermediate servers between client and server.
  7. **Code on Demand**: It is optional feature according to these cyber can also provide executable code to the client.

* *REST-API Basic coding*
  1. put
  2. get
  3. patch
  4. delete

  ## Code Type
  comming
  
