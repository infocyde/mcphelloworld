from mcp.server.fastmcp import FastMCP
import yfinance as yf

mcp = FastMCP("Simple Calculator Server")


# simple test functions 
@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b

@mcp.tool()
def subtract(a:int, b:int) -> int:
    return a-b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    return a*b

@mcp.tool()
def divide(a:float, b:float) -> float:
    # check divide by zero
    if b ==0:
        raise ValueError("div by zero error")
    return a/b 

@mcp.tool()
def gold_spot_price() -> dict:
    ticker = yf.Ticker("GC=F") #XAU
    info = ticker.info
    return info
    # if 'regularMarketOpen' not in info:
    #     raise ValueError("Unable to fetch gold spot price; check ticker or network.")
    # return str(info['regularMarketOpen'])



if __name__ == "__main__":
    mcp.run(transport="stdio")   
