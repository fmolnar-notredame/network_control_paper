i = 0
with open("rgn_markup.txt", "w") as f:
    f.write("<table>\n")
    for r in range(200):
        if i > 702:
            break
        f.write("  <tr>\n")
        for c in range(4):
            i += 1
            if i > 702:
                break
            f.write('    <td> %d <img src="fig/FigSI_RGG_SIN_%d.png" </td>\n' % (i,i))
        f.write("  </tr>\n")
    f.write("</table>\n")
print("Done")
