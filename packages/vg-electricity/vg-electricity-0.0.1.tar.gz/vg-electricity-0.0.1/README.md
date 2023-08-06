# vg-electricity-py



## Getting started

```python
async def main():
    vg = VGEl()
    print(await vg.sensor_data())
    await vg.close_session()

asyncio.run(main())
```