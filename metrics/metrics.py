import argparse
def results(metrics):
  import joblib
  data=joblib.load(metrics)
  print(f"{data['score']} \n")
  print(f"{data['cm']} \n")
  print(f"{data['cr']} \n")
  with open('results.txt','w') as result:
    result.write(f'Accuracy {data['score']}  \n\n Confusion matrix {data['cm']} \n\n Classification report {data['cr']}')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--metrics')
  args = parser.parse_args()
  results(args.metrics)