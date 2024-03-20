/**
 * Animation variants
 * @link https://www.framer.com/motion/animation/#variants
 */

const transition = {
  type: "tween",
  ease: "easeInOut",
  duration: 0.25,
}

export const modal = {
  show: {
    opacity: 1,
    transition,
  },
  hide: {
    opacity: 0,
    transition,
  },
}
