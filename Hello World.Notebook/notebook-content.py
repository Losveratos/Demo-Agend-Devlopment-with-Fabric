# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Hello World 👋
# Ein einfaches Demo-Notebook, erstellt über den Agent-Git-Workflow.

# CELL ********************

print("Hallo Welt! 👋")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Kleines PySpark-Beispiel: ein Mini-DataFrame anzeigen
df = spark.createDataFrame(
    [("Hallo", "Welt"), ("Hello", "World")],
    ["gruss", "ziel"],
)
df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
