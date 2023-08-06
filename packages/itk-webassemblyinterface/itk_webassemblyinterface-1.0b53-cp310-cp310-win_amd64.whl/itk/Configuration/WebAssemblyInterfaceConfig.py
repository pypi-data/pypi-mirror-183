depends = ('ITKPyBase', 'MeshToPolyData', 'ITKImageFunction', 'ITKIOMeshBase', 'ITKIOImageBase', 'ITKCommon', )
templates = (  ('WASMImageIO', 'itk::WASMImageIO', 'itkWASMImageIO', True),
  ('WASMImageIOFactory', 'itk::WASMImageIOFactory', 'itkWASMImageIOFactory', True),
  ('WASMMeshIO', 'itk::WASMMeshIO', 'itkWASMMeshIO', True),
  ('WASMMeshIOFactory', 'itk::WASMMeshIOFactory', 'itkWASMMeshIOFactory', True),
)
factories = (("ImageIO","WASM"),("MeshIO","WASM"),)
