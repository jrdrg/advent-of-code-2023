import util
import functools

example_input = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

input_str = """
6,9,184~8,9,184
7,0,46~9,0,46
4,2,78~4,5,78
0,4,182~0,6,182
7,4,249~7,6,249
4,0,47~7,0,47
6,3,182~9,3,182
0,3,162~3,3,162
3,8,127~6,8,127
2,0,246~2,1,246
8,4,248~8,6,248
5,4,166~7,4,166
1,7,2~1,9,2
5,0,254~5,2,254
2,4,257~2,4,260
7,0,211~7,1,211
3,6,241~3,8,241
1,6,130~3,6,130
7,4,56~9,4,56
6,4,270~8,4,270
7,7,102~8,7,102
7,8,23~8,8,23
1,5,60~4,5,60
9,8,23~9,9,23
3,2,116~3,3,116
4,3,27~4,6,27
8,6,163~8,9,163
9,5,5~9,8,5
0,6,195~0,6,197
4,2,134~7,2,134
0,9,68~3,9,68
7,4,244~7,4,244
5,5,243~6,5,243
6,4,201~6,6,201
6,1,2~7,1,2
7,4,16~8,4,16
6,7,251~8,7,251
2,4,118~2,4,121
1,4,262~2,4,262
5,1,188~5,3,188
4,3,49~6,3,49
3,7,55~6,7,55
2,1,36~2,1,38
5,9,114~5,9,114
7,6,59~7,8,59
6,1,230~7,1,230
6,4,242~6,6,242
6,3,185~6,3,187
6,0,40~6,2,40
5,6,45~8,6,45
7,6,42~7,8,42
0,3,42~2,3,42
2,8,257~2,9,257
8,3,110~8,5,110
2,9,277~4,9,277
3,4,260~5,4,260
0,5,34~2,5,34
5,7,69~7,7,69
0,5,133~2,5,133
3,7,165~4,7,165
6,6,109~6,8,109
2,4,240~5,4,240
5,4,130~7,4,130
2,4,3~2,4,5
9,9,121~9,9,123
1,4,176~1,5,176
4,1,227~6,1,227
9,2,189~9,2,190
5,5,157~6,5,157
3,3,226~3,5,226
6,4,128~8,4,128
0,6,93~0,8,93
8,0,213~9,0,213
7,3,213~7,5,213
6,1,166~6,1,166
0,3,273~0,5,273
8,0,216~9,0,216
7,8,247~8,8,247
1,6,266~1,8,266
1,3,251~2,3,251
0,7,197~0,9,197
6,2,172~6,5,172
5,3,265~7,3,265
0,0,101~2,0,101
0,9,17~2,9,17
3,5,15~3,7,15
3,2,119~5,2,119
4,8,262~4,8,263
3,3,207~3,5,207
3,4,244~5,4,244
6,8,161~9,8,161
6,3,32~6,5,32
7,5,164~7,7,164
4,0,255~4,1,255
7,1,61~7,3,61
6,5,60~6,6,60
0,3,257~2,3,257
5,7,202~5,7,205
7,2,35~7,2,36
6,5,13~8,5,13
7,6,242~7,8,242
8,5,165~8,6,165
0,3,101~0,5,101
6,7,4~8,7,4
7,6,254~7,8,254
4,2,229~4,3,229
4,2,124~4,2,124
6,6,74~6,9,74
1,3,94~1,5,94
9,3,183~9,5,183
9,4,206~9,6,206
3,2,69~3,4,69
9,3,49~9,4,49
5,2,209~7,2,209
2,1,207~4,1,207
6,2,149~6,5,149
0,5,163~0,7,163
4,4,74~7,4,74
7,7,175~9,7,175
5,3,260~7,3,260
2,4,276~2,4,279
0,1,174~2,1,174
6,2,206~6,4,206
4,3,118~5,3,118
7,1,236~7,2,236
1,6,6~1,8,6
3,0,69~5,0,69
2,4,275~3,4,275
4,0,50~4,1,50
0,4,134~0,6,134
3,1,229~5,1,229
0,9,66~2,9,66
2,3,132~2,3,133
1,6,141~1,9,141
0,3,167~2,3,167
4,2,22~4,4,22
6,1,277~6,3,277
2,6,70~2,9,70
1,1,216~3,1,216
0,8,172~2,8,172
4,6,243~4,8,243
4,5,113~5,5,113
4,6,28~6,6,28
7,1,44~7,1,46
3,4,201~3,5,201
7,6,21~9,6,21
3,6,273~5,6,273
6,7,42~6,9,42
4,0,66~4,1,66
9,3,134~9,4,134
2,3,81~2,4,81
1,7,86~2,7,86
2,3,79~3,3,79
4,4,176~4,6,176
2,4,219~4,4,219
4,6,67~4,6,68
3,3,160~5,3,160
0,9,194~3,9,194
8,1,152~8,3,152
2,0,23~2,0,24
5,0,3~5,2,3
5,0,11~5,1,11
6,4,6~6,6,6
0,8,88~1,8,88
5,6,139~7,6,139
0,6,22~0,7,22
8,2,251~8,4,251
2,4,153~2,6,153
1,0,15~1,2,15
9,0,234~9,2,234
5,0,12~5,1,12
4,3,275~5,3,275
3,7,273~6,7,273
4,6,97~6,6,97
6,9,239~6,9,241
4,1,147~5,1,147
9,3,58~9,5,58
8,6,69~8,6,71
7,6,140~7,9,140
7,1,197~9,1,197
7,2,63~9,2,63
3,2,12~3,3,12
7,5,33~7,8,33
3,3,276~3,6,276
0,1,166~1,1,166
4,7,129~4,8,129
3,4,20~3,4,22
1,3,32~4,3,32
2,1,66~2,1,68
1,3,158~1,5,158
2,2,46~6,2,46
0,2,46~0,4,46
9,2,139~9,2,139
0,7,198~1,7,198
3,1,7~3,1,10
5,3,101~5,6,101
9,0,148~9,1,148
6,2,250~6,2,252
5,5,31~5,7,31
3,4,169~3,6,169
3,9,6~4,9,6
4,1,121~4,2,121
0,3,2~2,3,2
5,7,197~7,7,197
8,9,10~8,9,10
1,0,74~1,2,74
5,0,203~5,3,203
3,6,217~3,6,219
7,4,79~7,5,79
0,6,166~4,6,166
3,3,93~3,6,93
6,8,236~6,9,236
8,0,119~8,3,119
2,1,149~2,3,149
0,8,206~0,8,206
9,2,29~9,2,31
1,8,58~2,8,58
2,7,235~2,9,235
4,3,164~4,4,164
0,2,271~0,5,271
3,4,264~3,7,264
5,9,103~6,9,103
6,5,195~8,5,195
3,9,144~6,9,144
3,6,158~3,8,158
0,4,183~0,7,183
4,5,242~4,9,242
0,4,156~2,4,156
3,0,257~3,2,257
0,4,57~2,4,57
6,5,170~9,5,170
3,2,114~3,4,114
1,2,176~1,3,176
2,1,153~5,1,153
0,3,268~3,3,268
3,7,105~3,7,107
6,3,280~9,3,280
4,6,120~4,8,120
5,7,235~5,9,235
8,6,124~8,6,126
2,6,177~5,6,177
8,8,230~9,8,230
0,2,60~0,4,60
6,4,269~8,4,269
9,4,28~9,7,28
0,4,130~2,4,130
8,4,120~8,5,120
5,5,102~7,5,102
1,0,189~3,0,189
4,4,25~6,4,25
0,3,244~2,3,244
3,0,10~5,0,10
4,2,95~4,4,95
0,2,195~2,2,195
1,3,5~1,4,5
2,8,260~4,8,260
5,7,23~5,8,23
5,4,143~5,6,143
2,9,243~2,9,244
7,5,18~9,5,18
1,6,65~1,7,65
3,8,50~3,9,50
3,5,110~3,8,110
6,8,281~7,8,281
6,7,249~8,7,249
2,1,33~2,3,33
3,6,103~3,8,103
5,6,218~5,8,218
6,0,114~6,3,114
2,7,253~4,7,253
2,7,100~2,7,101
6,3,178~6,5,178
3,2,245~4,2,245
3,6,239~3,8,239
1,7,195~1,9,195
5,5,83~5,8,83
8,5,289~8,8,289
6,7,221~9,7,221
1,5,199~1,6,199
0,3,38~3,3,38
3,0,39~3,1,39
7,4,243~7,6,243
1,8,178~1,8,181
6,4,89~6,4,91
3,3,247~3,6,247
0,2,159~0,4,159
3,7,98~5,7,98
2,9,214~4,9,214
9,1,219~9,3,219
0,2,256~0,2,258
7,4,193~7,5,193
7,0,235~7,1,235
1,1,159~1,3,159
3,2,202~3,4,202
1,1,256~3,1,256
0,6,162~0,8,162
9,8,86~9,9,86
8,4,116~8,6,116
5,0,224~5,3,224
1,0,195~2,0,195
4,8,183~7,8,183
8,4,191~9,4,191
5,6,243~5,8,243
2,4,211~2,6,211
0,9,2~0,9,2
4,0,257~4,3,257
5,5,53~8,5,53
3,5,66~4,5,66
2,3,125~4,3,125
7,3,82~7,5,82
9,1,26~9,3,26
7,6,245~7,8,245
5,5,76~6,5,76
9,3,70~9,3,71
9,6,247~9,6,247
0,1,5~3,1,5
4,8,238~5,8,238
8,2,66~9,2,66
3,4,13~5,4,13
0,0,103~0,3,103
3,7,53~3,9,53
6,7,275~8,7,275
3,5,74~6,5,74
2,3,88~2,6,88
6,4,56~6,4,58
0,7,19~0,9,19
2,1,87~2,2,87
0,0,98~2,0,98
5,4,193~6,4,193
9,7,241~9,9,241
7,2,41~8,2,41
1,7,87~1,9,87
5,0,53~5,1,53
3,3,39~3,5,39
6,1,99~6,3,99
6,1,194~6,4,194
4,4,104~6,4,104
4,4,28~6,4,28
4,3,232~7,3,232
9,4,274~9,6,274
0,3,226~2,3,226
3,2,41~4,2,41
6,5,3~6,5,4
5,3,273~7,3,273
3,3,50~6,3,50
7,7,232~9,7,232
5,2,148~5,4,148
5,8,43~8,8,43
9,1,145~9,3,145
1,4,91~3,4,91
9,2,111~9,4,111
3,3,214~4,3,214
4,5,240~6,5,240
6,7,162~8,7,162
4,8,20~7,8,20
7,9,9~8,9,9
2,8,6~2,9,6
6,9,249~8,9,249
6,0,189~6,3,189
5,1,278~8,1,278
4,4,174~4,6,174
6,5,20~7,5,20
9,3,189~9,3,189
1,5,56~1,9,56
4,2,222~4,4,222
6,5,48~6,7,48
7,2,30~7,5,30
5,3,124~5,5,124
2,1,198~4,1,198
7,1,132~9,1,132
5,2,259~5,4,259
6,7,13~6,7,15
1,3,142~2,3,142
5,7,80~5,8,80
2,6,64~2,9,64
8,5,259~8,8,259
1,2,60~1,4,60
0,5,54~0,8,54
0,1,18~0,1,19
0,1,41~1,1,41
7,6,199~7,8,199
9,1,213~9,3,213
3,7,47~5,7,47
9,6,22~9,8,22
9,2,275~9,4,275
0,7,166~2,7,166
3,6,156~6,6,156
3,6,79~3,8,79
4,4,210~5,4,210
0,1,62~0,4,62
5,2,84~7,2,84
6,1,163~6,3,163
7,0,174~7,3,174
8,1,212~8,3,212
1,5,129~4,5,129
7,7,257~9,7,257
0,0,199~2,0,199
7,3,262~8,3,262
3,5,180~3,6,180
8,2,204~8,4,204
0,8,55~1,8,55
3,4,198~6,4,198
6,4,142~6,6,142
0,4,255~2,4,255
1,6,96~1,8,96
5,1,87~6,1,87
4,8,81~6,8,81
7,6,179~7,8,179
7,5,274~7,5,277
3,0,229~6,0,229
9,5,217~9,5,219
2,6,144~2,8,144
6,2,249~6,5,249
2,8,189~4,8,189
5,0,61~7,0,61
7,3,124~7,5,124
6,1,96~6,3,96
8,8,25~9,8,25
0,7,91~0,8,91
7,1,64~7,1,67
9,0,192~9,2,192
5,7,220~5,7,222
2,5,51~4,5,51
6,9,268~6,9,271
2,4,8~5,4,8
4,3,7~6,3,7
6,8,125~8,8,125
4,0,250~6,0,250
9,5,102~9,8,102
3,1,221~3,1,223
5,2,182~5,2,184
2,0,267~5,0,267
0,4,179~1,4,179
6,7,99~9,7,99
7,5,221~7,6,221
1,6,239~2,6,239
3,9,15~6,9,15
8,6,122~8,8,122
2,5,238~2,7,238
2,4,234~2,7,234
2,0,4~3,0,4
1,1,150~3,1,150
8,0,282~9,0,282
7,9,39~9,9,39
6,1,85~6,3,85
9,4,208~9,4,208
8,8,260~8,8,261
4,8,85~6,8,85
6,1,212~6,4,212
1,6,257~1,9,257
4,9,38~7,9,38
4,6,44~4,8,44
2,7,241~2,7,244
6,3,53~8,3,53
5,5,133~7,5,133
7,2,181~7,4,181
0,4,81~0,7,81
3,1,194~3,4,194
3,5,263~3,6,263
8,0,72~8,2,72
3,3,250~4,3,250
5,1,102~6,1,102
6,9,77~8,9,77
1,3,95~1,6,95
5,4,105~5,6,105
0,5,187~0,9,187
5,5,154~5,7,154
1,3,177~1,3,178
4,9,18~6,9,18
8,0,2~8,0,4
6,0,4~6,1,4
6,2,186~9,2,186
2,8,194~3,8,194
2,2,84~2,3,84
5,1,60~5,1,62
1,2,254~1,5,254
0,0,193~0,2,193
5,5,190~7,5,190
5,5,1~5,8,1
4,7,39~4,9,39
0,5,184~2,5,184
0,0,85~0,2,85
4,2,179~4,4,179
8,3,63~8,3,66
4,4,207~6,4,207
3,1,13~4,1,13
1,8,27~3,8,27
5,3,271~5,4,271
0,1,220~3,1,220
5,6,232~7,6,232
2,8,1~4,8,1
6,8,257~7,8,257
2,5,182~2,7,182
0,8,52~3,8,52
6,0,59~6,2,59
0,8,118~2,8,118
3,5,78~3,7,78
1,2,69~1,2,72
7,1,175~7,1,176
6,0,60~7,0,60
1,0,162~1,2,162
2,3,223~5,3,223
4,9,249~4,9,251
1,6,41~3,6,41
5,8,241~7,8,241
6,3,93~6,6,93
2,8,217~2,9,217
9,2,108~9,2,108
4,8,287~7,8,287
1,4,106~1,5,106
0,2,217~0,4,217
7,2,210~7,5,210
5,5,103~5,6,103
4,2,255~4,5,255
0,5,270~0,7,270
7,1,69~8,1,69
7,9,240~8,9,240
6,5,8~9,5,8
0,4,10~0,6,10
5,5,237~7,5,237
6,8,14~9,8,14
5,4,276~8,4,276
5,3,197~7,3,197
6,3,252~6,5,252
1,1,226~3,1,226
5,4,29~7,4,29
5,5,136~5,7,136
4,6,254~4,6,254
2,6,104~2,8,104
4,6,197~5,6,197
0,1,221~1,1,221
4,4,265~8,4,265
1,7,247~1,8,247
0,0,95~0,4,95
7,9,115~9,9,115
5,6,235~7,6,235
3,7,26~3,9,26
1,0,248~2,0,248
0,8,270~0,8,273
7,1,213~7,2,213
6,2,230~8,2,230
1,7,246~2,7,246
2,5,63~2,6,63
0,8,203~0,9,203
3,0,285~6,0,285
4,1,190~6,1,190
7,4,88~8,4,88
0,9,276~2,9,276
2,7,208~2,9,208
7,9,256~9,9,256
9,3,216~9,5,216
7,2,39~7,2,40
0,5,193~0,5,195
1,9,18~1,9,20
3,7,274~3,7,276
0,4,256~0,4,256
2,4,34~4,4,34
5,5,138~5,7,138
4,8,204~7,8,204
2,1,63~5,1,63
1,5,135~1,8,135
2,3,248~2,5,248
4,9,48~6,9,48
3,4,191~5,4,191
2,2,186~4,2,186
0,2,14~0,2,16
0,9,62~3,9,62
8,5,142~9,5,142
1,0,77~1,1,77
1,2,164~1,2,166
5,0,275~5,0,276
4,5,11~4,7,11
4,7,208~6,7,208
0,2,90~0,2,92
0,7,10~3,7,10
3,0,266~5,0,266
8,8,83~9,8,83
1,2,66~3,2,66
0,6,60~0,7,60
6,6,106~6,9,106
4,6,98~6,6,98
1,5,35~1,5,35
1,8,175~1,9,175
3,2,150~3,2,153
2,0,3~2,2,3
5,4,26~5,5,26
3,1,65~5,1,65
2,5,102~2,7,102
1,8,254~2,8,254
0,4,97~0,5,97
4,7,125~4,7,125
2,0,139~2,3,139
5,6,85~5,7,85
7,7,187~7,9,187
1,0,273~1,2,273
7,7,182~7,9,182
7,8,244~9,8,244
2,3,225~2,5,225
1,2,102~1,5,102
0,8,198~0,8,200
0,8,165~2,8,165
0,4,12~2,4,12
1,5,179~1,7,179
3,5,96~3,9,96
1,0,100~1,3,100
3,6,216~3,9,216
7,6,231~7,9,231
2,9,267~3,9,267
5,7,254~6,7,254
1,6,269~1,7,269
4,4,192~6,4,192
0,0,198~0,3,198
3,1,144~3,3,144
5,0,215~7,0,215
1,2,228~1,4,228
1,5,77~1,7,77
9,1,277~9,4,277
2,5,130~3,5,130
8,6,207~9,6,207
8,7,172~8,8,172
1,1,47~1,3,47
7,5,54~8,5,54
7,5,137~7,8,137
6,3,167~6,5,167
2,9,18~2,9,21
0,6,126~2,6,126
2,4,93~2,5,93
8,2,185~8,3,185
6,6,67~9,6,67
9,7,103~9,9,103
4,6,280~7,6,280
2,3,184~4,3,184
8,6,18~9,6,18
0,3,253~0,5,253
6,6,159~6,8,159
8,5,249~8,5,250
0,1,168~1,1,168
0,5,191~0,7,191
0,7,25~0,9,25
9,1,216~9,1,218
1,4,104~1,6,104
5,2,204~5,4,204
6,9,86~7,9,86
1,6,136~1,6,139
7,7,85~9,7,85
6,2,69~6,3,69
1,7,137~3,7,137
9,0,278~9,2,278
3,1,135~3,3,135
6,3,215~6,5,215
5,2,101~8,2,101
5,2,55~5,4,55
4,1,6~5,1,6
8,5,128~8,6,128
3,7,13~3,9,13
2,0,279~4,0,279
1,4,217~1,6,217
1,1,272~4,1,272
2,3,161~6,3,161
6,8,243~6,8,246
5,8,78~5,9,78
2,1,243~2,4,243
2,3,271~2,6,271
7,2,232~9,2,232
4,5,63~6,5,63
1,6,53~1,8,53
5,1,268~5,3,268
2,3,127~2,5,127
9,0,142~9,2,142
5,1,257~5,3,257
5,8,227~8,8,227
3,0,187~4,0,187
1,5,194~1,5,196
4,6,179~4,8,179
3,3,166~5,3,166
1,2,44~3,2,44
5,2,262~6,2,262
4,2,66~4,4,66
4,2,195~5,2,195
1,7,189~3,7,189
0,6,120~0,8,120
2,3,237~2,6,237
0,1,43~0,1,46
1,0,175~1,2,175
0,6,258~0,7,258
0,4,64~0,7,64
5,0,255~6,0,255
5,7,156~5,8,156
7,4,41~7,8,41
6,0,256~9,0,256
3,6,17~3,8,17
6,3,71~6,3,73
2,6,123~2,7,123
0,1,275~0,2,275
8,9,259~8,9,261
3,2,243~3,5,243
8,0,279~8,2,279
7,4,55~8,4,55
3,6,191~3,8,191
5,6,133~6,6,133
2,2,88~2,2,89
7,7,165~7,9,165
6,3,101~6,5,101
0,9,275~2,9,275
2,3,239~3,3,239
9,7,42~9,9,42
4,0,254~4,3,254
3,8,134~3,8,136
2,0,20~5,0,20
6,4,51~6,8,51
4,3,123~4,6,123
8,8,185~8,9,185
1,4,174~3,4,174
0,5,154~2,5,154
6,4,127~8,4,127
4,7,246~4,9,246
6,3,86~6,5,86
5,4,46~8,4,46
4,0,134~5,0,134
0,9,14~1,9,14
3,4,154~5,4,154
0,4,188~3,4,188
3,5,18~3,7,18
0,7,128~0,9,128
1,5,246~3,5,246
4,5,224~4,5,226
5,7,219~6,7,219
2,5,83~2,7,83
8,4,271~9,4,271
0,5,251~2,5,251
1,8,49~4,8,49
1,0,193~2,0,193
3,1,231~5,1,231
4,5,125~4,6,125
6,1,228~6,3,228
8,7,78~8,9,78
8,4,113~8,5,113
2,8,4~4,8,4
0,0,106~1,0,106
7,2,32~7,4,32
6,6,243~6,6,245
7,4,121~7,6,121
4,0,43~7,0,43
9,0,1~9,3,1
3,8,112~4,8,112
6,9,244~6,9,247
1,7,3~2,7,3
6,0,284~8,0,284
5,7,10~6,7,10
4,7,238~5,7,238
5,8,139~7,8,139
8,6,252~8,7,252
0,7,267~0,9,267
7,0,3~7,2,3
7,6,238~7,9,238
6,3,66~6,7,66
2,3,77~2,6,77
7,1,90~7,2,90
6,9,43~6,9,45
4,3,134~4,5,134
1,5,11~1,9,11
6,4,47~9,4,47
4,5,141~5,5,141
3,4,94~3,4,97
3,3,180~4,3,180
2,0,272~5,0,272
1,7,173~3,7,173
8,2,118~8,4,118
5,2,278~7,2,278
5,2,146~5,4,146
2,6,140~2,9,140
1,7,160~4,7,160
4,8,41~6,8,41
4,9,188~7,9,188
0,4,7~0,7,7
0,5,13~0,7,13
1,2,48~4,2,48
0,6,8~0,8,8
4,4,286~6,4,286
3,0,136~5,0,136
0,1,171~3,1,171
3,5,216~6,5,216
1,3,61~1,3,64
1,2,169~1,5,169
3,5,29~5,5,29
1,3,122~3,3,122
7,5,283~7,7,283
0,5,58~0,7,58
5,1,94~5,1,98
2,5,78~2,5,79
2,4,102~5,4,102
0,2,88~0,2,89
7,4,131~9,4,131
2,7,99~2,9,99
5,5,107~5,8,107
3,0,72~6,0,72
7,5,118~8,5,118
6,9,202~8,9,202
5,7,228~7,7,228
6,5,278~6,8,278
3,6,187~3,8,187
2,1,173~5,1,173
3,4,19~6,4,19
1,7,251~4,7,251
6,7,11~6,9,11
3,1,93~5,1,93
3,3,270~3,4,270
1,3,191~1,7,191
5,5,235~8,5,235
7,5,246~9,5,246
0,0,22~0,1,22
9,7,105~9,9,105
2,7,82~2,9,82
3,8,132~4,8,132
1,1,257~2,1,257
4,9,111~5,9,111
1,3,190~2,3,190
0,1,169~0,3,169
4,7,9~6,7,9
9,3,112~9,4,112
0,7,180~2,7,180
3,7,199~6,7,199
7,3,272~9,3,272
2,6,127~2,6,129
5,1,59~5,1,59
8,4,10~8,6,10
7,6,201~7,9,201
4,5,65~4,8,65
5,4,195~5,7,195
1,6,20~3,6,20
2,1,253~2,4,253
5,4,132~5,7,132
0,1,17~2,1,17
6,2,283~6,5,283
1,0,151~1,2,151
6,4,136~6,6,136
6,3,235~7,3,235
1,4,63~1,7,63
1,0,165~3,0,165
8,7,7~8,9,7
9,8,165~9,9,165
6,2,176~6,5,176
4,7,215~7,7,215
2,4,172~5,4,172
9,0,50~9,0,53
4,9,253~7,9,253
6,5,219~8,5,219
0,1,165~0,3,165
2,0,135~2,3,135
4,7,145~5,7,145
5,0,264~5,2,264
7,4,271~7,5,271
3,5,40~3,7,40
6,2,214~6,5,214
3,9,218~3,9,218
8,4,6~8,7,6
1,4,49~4,4,49
7,1,33~7,2,33
2,6,120~2,8,120
2,3,186~4,3,186
8,4,1~8,6,1
4,1,205~5,1,205
7,3,60~7,4,60
3,4,43~3,5,43
7,7,112~7,9,112
6,4,54~7,4,54
7,6,218~7,6,219
1,2,61~1,2,64
0,9,83~4,9,83
9,2,107~9,4,107
3,6,261~3,8,261
7,2,130~9,2,130
0,6,24~1,6,24
0,5,255~0,7,255
6,8,193~6,8,195
9,8,162~9,8,164
7,1,126~7,3,126
7,3,85~7,5,85
0,4,5~0,7,5
5,2,33~5,3,33
0,4,215~2,4,215
7,5,135~9,5,135
5,0,206~5,2,206
3,8,163~6,8,163
7,4,142~7,7,142
7,7,72~7,9,72
3,8,119~6,8,119
6,4,108~8,4,108
0,5,190~0,7,190
7,7,83~7,9,83
4,3,226~4,4,226
5,4,12~8,4,12
7,1,210~9,1,210
2,1,56~5,1,56
7,6,203~9,6,203
3,5,250~3,8,250
4,0,184~4,2,184
2,0,27~3,0,27
4,2,180~6,2,180
0,6,276~0,8,276
6,2,281~9,2,281
2,4,231~2,6,231
1,5,33~3,5,33
8,6,169~8,8,169
9,6,235~9,7,235
1,9,69~1,9,70
8,2,215~8,2,217
0,7,125~2,7,125
6,0,44~6,1,44
9,4,2~9,5,2
2,7,142~5,7,142
2,4,92~4,4,92
7,5,222~7,7,222
3,0,225~5,0,225
1,6,84~1,9,84
4,2,248~6,2,248
4,5,46~4,8,46
2,4,116~4,4,116
6,4,105~9,4,105
1,1,39~1,3,39
1,8,30~3,8,30
2,5,167~2,8,167
0,4,214~2,4,214
7,9,242~9,9,242
8,2,129~8,4,129
5,5,2~5,6,2
0,0,272~0,2,272
0,9,264~3,9,264
5,3,151~5,5,151
8,1,215~8,1,218
5,4,213~5,7,213
1,8,116~3,8,116
1,0,1~1,2,1
5,7,225~5,9,225
0,7,66~0,8,66
8,3,237~8,6,237
5,4,126~5,6,126
5,5,104~8,5,104
1,0,250~3,0,250
0,1,224~0,2,224
8,3,61~8,6,61
6,7,220~6,9,220
6,6,167~9,6,167
3,6,62~3,8,62
8,2,138~8,4,138
6,9,116~7,9,116
1,5,32~3,5,32
5,4,268~7,4,268
4,8,284~7,8,284
1,3,87~3,3,87
0,0,176~3,0,176
3,7,163~4,7,163
3,3,30~5,3,30
5,2,252~5,4,252
8,4,15~8,6,15
2,9,142~3,9,142
2,5,207~2,7,207
0,1,190~0,4,190
1,5,16~1,7,16
4,3,144~4,6,144
8,5,196~8,6,196
7,2,81~7,4,81
5,3,270~7,3,270
8,1,264~8,4,264
1,0,262~1,2,262
3,2,38~4,2,38
7,6,216~7,7,216
2,7,240~2,9,240
2,2,215~6,2,215
9,2,188~9,5,188
5,8,39~7,8,39
4,1,271~6,1,271
0,1,136~0,3,136
4,4,274~4,6,274
3,1,259~3,3,259
4,1,127~4,2,127
5,3,4~6,3,4
2,2,153~2,2,153
5,8,184~5,8,184
4,2,216~4,4,216
1,5,156~2,5,156
2,6,80~2,9,80
8,7,173~8,9,173
4,0,8~4,2,8
5,0,193~5,2,193
4,0,191~4,3,191
5,3,48~5,4,48
3,1,215~6,1,215
5,2,187~5,5,187
7,6,36~7,9,36
7,4,165~7,6,165
8,0,149~8,3,149
3,3,121~5,3,121
4,7,7~6,7,7
6,8,53~7,8,53
7,2,148~9,2,148
3,8,23~4,8,23
7,7,74~8,7,74
6,5,139~8,5,139
1,5,160~4,5,160
4,0,131~4,3,131
4,6,222~4,8,222
0,0,173~0,2,173
5,5,232~7,5,232
6,8,207~9,8,207
7,9,250~9,9,250
3,1,197~3,3,197
9,6,223~9,9,223
3,1,36~3,4,36
2,2,152~2,4,152
5,5,110~6,5,110
8,6,119~8,8,119
0,2,186~0,4,186
4,4,44~7,4,44
1,5,258~4,5,258
3,5,256~5,5,256
2,5,204~5,5,204
0,0,136~2,0,136
3,4,57~3,7,57
0,5,19~1,5,19
8,3,2~8,3,4
2,1,217~5,1,217
5,5,231~5,7,231
5,1,91~5,4,91
6,6,58~8,6,58
8,0,73~8,2,73
0,6,83~0,7,83
5,0,249~5,3,249
7,1,129~7,3,129
7,5,55~7,6,55
6,4,174~6,7,174
5,5,191~5,6,191
8,7,27~9,7,27
7,5,234~8,5,234
5,3,216~7,3,216
1,8,237~3,8,237
9,7,259~9,9,259
1,6,263~1,8,263
1,6,260~3,6,260
4,8,219~4,9,219
5,1,52~5,3,52
5,8,52~5,9,52
1,2,142~3,2,142
6,5,111~6,7,111
8,6,197~9,6,197
0,2,84~0,4,84
1,4,250~3,4,250
2,8,253~4,8,253
0,1,98~0,3,98
7,3,211~7,5,211
0,2,255~2,2,255
6,4,71~6,7,71
5,3,154~5,3,157
6,3,203~8,3,203
9,3,25~9,6,25
6,1,233~7,1,233
7,2,136~9,2,136
9,3,244~9,7,244
1,0,28~2,0,28
0,4,3~0,6,3
5,2,58~6,2,58
0,9,189~0,9,192
1,8,72~1,9,72
8,5,24~8,7,24
2,3,130~4,3,130
6,4,179~8,4,179
5,9,233~7,9,233
1,5,75~4,5,75
1,3,134~3,3,134
7,9,118~9,9,118
7,3,145~7,5,145
1,7,188~2,7,188
5,5,18~5,8,18
2,7,124~4,7,124
1,2,265~1,4,265
6,0,212~9,0,212
5,2,54~5,3,54
0,4,170~3,4,170
2,3,117~4,3,117
4,7,216~4,9,216
7,6,286~8,6,286
0,3,55~0,5,55
5,7,276~5,9,276
6,1,34~6,4,34
1,2,146~3,2,146
3,4,32~5,4,32
2,7,14~4,7,14
4,0,228~7,0,228
1,9,269~3,9,269
1,1,181~1,3,181
4,6,54~7,6,54
5,2,32~5,3,32
4,1,53~4,3,53
1,7,184~4,7,184
6,0,37~6,3,37
0,2,13~3,2,13
3,6,70~5,6,70
5,1,42~7,1,42
5,9,51~7,9,51
4,2,252~4,6,252
3,2,225~5,2,225
1,3,9~4,3,9
7,6,248~7,7,248
2,8,98~3,8,98
6,7,229~6,8,229
6,4,76~7,4,76
0,1,260~2,1,260
7,3,234~7,4,234
1,5,14~1,7,14
1,2,16~1,2,19
1,2,65~4,2,65
2,6,262~2,9,262
4,9,109~6,9,109
5,2,2~5,4,2
4,3,213~4,4,213
5,2,88~7,2,88
7,1,195~9,1,195
0,0,18~2,0,18
5,8,82~8,8,82
7,3,172~7,5,172
4,4,48~4,6,48
3,2,148~3,5,148
7,7,108~7,7,110
5,4,16~5,6,16
0,6,154~2,6,154
2,1,146~6,1,146
4,0,277~6,0,277
2,7,186~2,9,186
1,0,191~3,0,191
0,5,258~0,5,260
6,5,98~8,5,98
3,8,114~4,8,114
8,2,189~8,5,189
7,7,105~7,9,105
1,6,214~3,6,214
7,5,71~7,8,71
2,5,2~4,5,2
2,4,274~2,6,274
5,6,128~7,6,128
3,4,118~3,5,118
2,8,100~5,8,100
5,7,178~7,7,178
3,6,59~4,6,59
5,3,200~6,3,200
8,7,166~8,7,168
0,3,161~0,6,161
3,1,51~3,3,51
4,4,194~4,6,194
5,1,131~9,1,131
1,1,3~1,2,3
3,7,27~3,7,30
2,9,211~4,9,211
0,5,192~0,7,192
5,8,222~7,8,222
1,1,11~3,1,11
1,9,242~2,9,242
4,7,198~6,7,198
6,7,179~6,7,181
2,2,189~2,3,189
0,4,280~3,4,280
6,0,5~6,2,5
1,6,169~1,9,169
3,3,54~3,3,57
2,2,257~2,2,258
1,9,272~3,9,272
4,0,268~4,0,270
5,1,208~7,1,208
9,6,101~9,9,101
1,1,140~3,1,140
7,3,56~7,3,59
6,7,2~6,9,2
2,2,35~2,3,35
1,5,255~3,5,255
6,3,113~8,3,113
0,2,43~0,4,43
3,7,59~3,9,59
9,9,25~9,9,27
5,4,270~5,7,270
2,5,229~3,5,229
0,2,135~0,4,135
9,0,47~9,1,47
0,1,227~0,2,227
4,5,223~4,7,223
1,6,15~2,6,15
2,6,210~5,6,210
9,6,238~9,9,238
3,9,266~6,9,266
4,3,283~4,6,283
2,5,273~4,5,273
6,5,96~6,8,96
6,8,190~7,8,190
3,1,185~6,1,185
5,7,139~7,7,139
5,7,102~5,9,102
6,7,78~6,9,78
5,5,12~5,8,12
7,7,43~7,7,44
6,1,147~6,3,147
5,6,29~7,6,29
1,6,170~1,8,170
6,4,182~6,6,182
0,6,14~0,7,14
6,4,221~6,6,221
4,5,228~4,7,228
5,5,32~5,5,32
3,4,112~3,6,112
0,6,92~0,8,92
7,6,15~7,8,15
6,3,274~6,6,274
3,9,2~3,9,4
3,3,165~3,6,165
5,8,76~7,8,76
3,9,151~5,9,151
0,4,78~2,4,78
7,4,223~7,6,223
5,9,145~5,9,148
4,1,183~4,3,183
9,1,68~9,4,68
"""

Coord3d = tuple[int, int, int]

def line_to_coords(line: str):
    start, end = line.split("~")
    sx, sy, sz = start.split(",")
    ex, ey, ez = end.split(",")
    return ((int(sx), int(sy), int(sz)), (int(ex), int(ey), int(ez)))

def add_brick_to_grid(grid: dict[Coord3d, str], brick: tuple[str, tuple[Coord3d, Coord3d]]):
    brick_id, ((sx, sy, sz), (ex, ey, ez)) = brick
    for z in range(sz, ez + 1):
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                grid[(x, y, z)] = brick_id
    return grid


def get_bounds(grid: dict[Coord3d, str]):
    bounds = (0, 0, 0)
    for coord in grid:
        bounds = (max(coord[0], bounds[0]), max(coord[1], bounds[1]), max(coord[2], bounds[2]))
    return bounds

def fall_downward(orig_grid: dict[Coord3d, str]):
    grid = orig_grid.copy()
    by_id = {}
    for coord in grid:
        by_id[grid[coord]] = by_id.get(grid[coord], [])
        by_id[grid[coord]].append(coord)

    # for b in by_id:
    #     print(b, by_id[b])

    def attempt_move(brick: str):
        old_pos = by_id[brick]
        new_pos = []
        for coord in old_pos:
            x, y, z = coord
            if z <= 1:
                return old_pos
            new_coord = (x, y, z - 1)
            if grid.get(new_coord) != None and grid.get(new_coord) != brick:
                return old_pos
            new_pos.append(new_coord)
        return new_pos

    def move_down():
        bricks = by_id.keys()
        moved = True
        while moved:
            moved = False
            for b in bricks:
                old_pos = by_id[b]
                new_pos = attempt_move(b)
                if new_pos != old_pos:
                    by_id[b] = new_pos
                    for c in old_pos:
                        grid[c] = None
                    for c in new_pos:
                        grid[c] = b
                    moved = True
    
    move_down()
    return grid


def remove_brick(brick: str, grid: dict[Coord3d, str]):
    new_grid = {}
    for coord in grid:
        if grid[coord] != brick:
            new_grid[coord] = grid.get(coord)
    return new_grid

def determine_removable_bricks(grid: dict[Coord3d, str]):
    bricks = sorted(set([grid[coord] for coord in grid if grid.get(coord) != None]))
    can_remove = []
    for b in bricks:
        print("Checking if brick can be removed:", b)
        g = grid.copy()
        g = remove_brick(b, g)
        new_g = fall_downward(g)
        if g == new_g:
            can_remove.append(b)
    return can_remove




def debug(grid: dict[Coord3d, str]):
    bx, by, bz = get_bounds(grid)
    out_zy = []
    out_zx = []
    print("Bounds", bx, by, bz)
    for z in range(0, bz+1):
        row = []
        for x in range(0, bx+1):
            brick = None
            row.append(".")
            for y in range(0, by+1):
                brick = grid.get((x, y, z))
                if brick != None:
                    row[x] = "?" if row[x] != brick and row[x] != "." else brick
        out_zx.append("".join(row))

        row = []
        for y in range(0, by+1):
            brick = None
            row.append(".")
            for x in range(0, bx+1):
                brick = grid.get((x, y, z))
                if brick != None:
                    row[y] = "?" if row[y] != brick and row[y] != "." else brick
        out_zy.append("".join(row))


    print("\n$$$\n")
    print("\n".join(reversed(out_zx)))
    print("\n---\n")
    print("\n".join(reversed(out_zy)))
    print("\n$$$\n")

def part1():
    lines = util.get_lines(input_str)
    coords = [(chr(i+65), line_to_coords(l)) for i, l in enumerate(lines)]

    grid = functools.reduce(add_brick_to_grid, coords, {})
    grid = fall_downward(grid)

    rem = determine_removable_bricks(grid)
    return len(rem)

print("Part 1", part1())
