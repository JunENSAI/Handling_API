from zeep import Client
from zeep.exceptions import Fault

def run_soap_client():
    wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
    client = Client(wsdl=wsdl)

    try:
        print("Available operations by service/port :")
        for service_name, service in client.wsdl.services.items():
            print(f"Service: {service_name}")
            for port in service.ports.values():
                print(f"  Port: {port.name}")
                for op_name, op_obj in port.binding._operations.items():
                    print(f"    - {op_name}")


        a, b = 25, 12

        print(f"\Call Add({a}, {b})…")
        result_add = client.service.Add(intA=a, intB=b)
        print("Result Add:", result_add)

        print(f"\nCall Multiply({a}, {b})…")
        result_mul = client.service.Multiply(intA=a, intB=b)
        print("Result Multiply:", result_mul)

    except Fault as fault:
        print("Erreur SOAP:", fault)
    except Exception as exc:
        print("Connexion error/execution:", exc)

if __name__ == "__main__":
    run_soap_client()
