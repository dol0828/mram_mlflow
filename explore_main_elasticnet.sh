for alpha in 0.45 0.55 0.65 0.75 0.85 ; do
  for l1_ratio in 0.25 0.5 0.75 ; do
    echo "============================================="
    echo "python main_elasticnet.py $alpha $l1_ratio"
    echo "============================================="
    python main_elasticnet.py $alpha $l1_ratio
  done
done
