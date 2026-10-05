from fastapi import FastAPI

app = FastAPI(title="CP03 - Azure VNet")

@app.get("/")
def home():
    return {
        "projeto": "CP03 - Azure VNet",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": "Microsoft Azure"
    }

@app.get("/network")
def network():
    return {
        "vnet": "vnet-cp03",
        "address_space": "10.10.0.0/16",
        "subnet": "10.10.2.0/23",
        "security": "NSG + VNet Integration"
    }