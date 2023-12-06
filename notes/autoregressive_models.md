# Autoregressive Models


Autoregressive models exploit the fact that we can write any probability
distribution as a product of conditional distributions using the chain
rule of probabilities
<sup><sup>source : C. M. Bishop, Pattern Recognition and Machine Learning, M.Jordan, J. Kleinberg, and B. Schölkopf, Eds., ser. Information science and Statistics. Springer, 2006, ch. Graphical. doi: 10.1117/1.2819119.<sup><sup>


$$
p(X) = \prod_{i=1}p(x_i | x_{<i})
$$

where xi is the i-th entry of the vector $x$ and $x<i$ corresponds to all previous entries in an arbitrary order.
A stationarity assumption is easily incorporated by using the same conditional distribution $p(xi | x<i )$ at every location.These two assumptions are often reasonable and can drastically reduce the amount of parameters of a model.



## Autoregressive Models in Lossless Compression

### Fundamental Concept
- Decomposes high-dimensional distributions into lower-dimensional conditional distributions.
- Predicts each element $x_i$ based on preceding elements $x_<i$.

### Applications in Different Data Modalities
- Useful for sequential data like audio or text. Example: Recurrent neural networks in text compression.
- Implemented in image compression (e.g., JPEG).

### Neural Network Extensions
- Nonlinear transformation of inputs in models like RNADE, PixelRNN, PixelCNN++.
- Advanced models like Image Transformer and PixelSNAIL use self-attention architectures.

### Dynamic vs. Static Models
- Static models have fixed parameters; dynamic models update parameters based on encoded data.
- Example of dynamic model: Wu et al.'s approach using linear predictors with dynamic parameters.

### Sequential Nature and Decoding
- Inherently sequential processing; each symbol depends on previously decoded symbols.
- Improved decoding speed by restricting context and increasing parallelism.

### Flexibility and Efficiency
- Incorporation of Markov or stationarity assumptions to reduce parameters.
- Well-suited for combination with arithmetic coding for sequential data handling..