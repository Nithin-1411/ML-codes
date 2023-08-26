import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the data into a pandas DataFrame
data_frame = pd.read_excel(r"C:\Users\G NITHIN\Documents\Machine_learning\Lab Session1 Data.xlsx", sheet_name="Purchase data")
df=data_frame.iloc[0:10,0:5]

# Create a new column 'Label' based on the Payment criterion
df['Label'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')
print(df)
# Separate features (X) and labels (y)
X = df.drop(['Customer', 'Payment (Rs)', 'Label'], axis=1)
y = df['Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test_scaled)

# Print classification report
print(classification_report(y_test, y_pred))
