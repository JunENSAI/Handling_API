## 1. What is SOAP?
**SOAP** (Simple Object Access Protocol) is a protocol for exchanging structured information. Unlike REST (which is an architectural style), SOAP is a strict protocol with heavy rules.

While REST uses lightweight JSON, SOAP uses **XML** (Extensible Markup Language).

---

### 2. The Envelope Structure

A SOAP message is not just raw data; it is wrapped in layers, like a physical letter:

1.  **Envelope:** The root element that defines the XML document as a SOAP message.

2.  **Header:** Meta-information (authentication credentials, complex transaction IDs).

3.  **Body:** The actual message/request details.

---

### 3. The WSDL (The Contract)
The most important concept in SOAP is the **WSDL** (Web Services Description Language). 

* **In REST:** You often guess the data structure or read a PDF documentation.

* **In SOAP:** The server provides a `.wsdl` file. This is a machine-readable XML file that describes *exactly* every function, every parameter, and every return type. 

Because of the WSDL, Python tools can "read" the API and automatically generate code for you. You rarely write raw XML manually; you let the library read the WSDL and create Python functions dynamically.

---

### 4. Why learn this in 2025?

* **Enterprise:** Banks, Airlines, and Telelcoms built their backends in the 2000s using SOAP. They still run on it.

* **Strictness:** SOAP supports ACID transactions and formal contracts, which is preferred for financial transfers.

---

### 5. The Tool: `zeep`

We will use the `zeep` library. It is the modern, high-performance SOAP client for Python. It parses the WSDL and creates a Python object that acts like the remote server.

---